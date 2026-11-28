import sqlite3
import json
import os
import sys
import subprocess
from datetime import datetime

# Fix Windows console encoding
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


DB_PATH = os.path.join(os.path.expanduser("~"), ".codex", "thread_history_1.sqlite")
INDEX_PATH = os.path.join(os.path.expanduser("~"), ".codex", "session_index.jsonl")

ALPHAAI_KEYWORDS = ['qwen', 'cloudflare', 'alibaba group', 'alphaai', 'pulselat']
ALPHAAI_MODEL_PREFIXES = ['cloudflare/', '@cf/', 'qwen', 'deepseek', 'llama', 'mistral', 'gemma', 'phi', 'falcon', 'mixtral']

def load_session_index(path):
    index = {}
    if not os.path.exists(path):
        return index
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    d = json.loads(line)
                    index[d['id']] = d
                except Exception:
                    pass
    return index

def is_alphaai(cur, thread_id):
    cur.execute("SELECT count(1) FROM thread_items WHERE thread_id=? AND item_json LIKE '%alphaai%'", (thread_id,))
    if cur.fetchone()[0] > 0:
        return True
    cur.execute("SELECT item_json FROM thread_items WHERE thread_id=? AND item_type='agentMessage' LIMIT 10", (thread_id,))
    for (ijson,) in cur.fetchall():
        try:
            text = json.loads(ijson).get('text', '').lower()
            if any(k in text for k in ALPHAAI_KEYWORDS):
                return True
        except Exception:
            pass
    return False

def get_first_user_message(cur, thread_id):
    cur.execute("""
        SELECT item_json FROM thread_items
        WHERE thread_id=? AND item_type='userMessage'
        ORDER BY rollout_ordinal ASC LIMIT 1
    """, (thread_id,))
    row = cur.fetchone()
    if not row:
        return ""
    try:
        d = json.loads(row[0])
        for c in d.get('content', []):
            if isinstance(c, dict) and 'text' in c:
                return c['text'].replace('\x00', ' ').replace('\n', ' ').strip()
    except Exception:
        pass
    return ""

def list_default_threads():
    if not os.path.exists(DB_PATH):
        print(f"[ERROR] No se encontró la base de datos de Codex en: {DB_PATH}", file=sys.stderr)
        sys.exit(1)

    session_index = load_session_index(INDEX_PATH)
    conn = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    cur = conn.cursor()

    cur.execute("SELECT thread_id, count(1), max(created_at_ms) FROM thread_items GROUP BY thread_id")
    all_threads = cur.fetchall()

    results = []
    for thread_id, item_count, max_ts in all_threads:
        if is_alphaai(cur, thread_id):
            continue
        idx = session_index.get(thread_id, {})
        title = idx.get('thread_name', '') or get_first_user_message(cur, thread_id) or 'Sin título'
        title = title.replace('\x00', ' ').replace('\n', ' ').strip()
        date_dt = datetime.fromtimestamp(max_ts / 1000.0) if max_ts else None
        results.append({
            'id': thread_id,
            'title': title,
            'date_str': date_dt.strftime('%Y-%m-%d %H:%M') if date_dt else '?',
            'timestamp': max_ts or 0,
            'item_count': item_count,
        })

    conn.close()
    results.sort(key=lambda x: x['timestamp'], reverse=True)
    return results

def interactive_picker(threads):
    print("\n+======================================================================+")
    print("|        CODEX - Sesiones (Perfil Default / OpenAI)                  |")
    print("+======================================================================+")
    for i, t in enumerate(threads, 1):
        title_short = t['title'][:52].ljust(52)
        print(f"| {i:3}. [{t['date_str']}]  {title_short} |")
        if i % 25 == 0 and i < len(threads):
            resp = input("|  [Enter] para ver mas, o escribe un numero: ").strip()
            if resp.isdigit():
                return int(resp)
    print("+======================================================================+")

    while True:
        try:
            resp = input(f"\nElige el numero del chat a retomar [1-{len(threads)}] o 'q' para salir: ").strip()
            if resp.lower() == 'q':
                print("Saliendo...")
                sys.exit(0)
            n = int(resp)
            if 1 <= n <= len(threads):
                return n
            print(f"Por favor elige entre 1 y {len(threads)}")
        except ValueError:
            print("Escribe un numero valido.")
        except KeyboardInterrupt:
            print("\nCancelado.")
            sys.exit(0)

def main():
    # If an ID or number is passed as arg, resume directly
    arg = sys.argv[1] if len(sys.argv) > 1 else None

    threads = list_default_threads()

    if not threads:
        print("No se encontraron sesiones del perfil default de Codex.")
        sys.exit(1)

    if arg:
        # Try to match by index number
        if arg.isdigit():
            n = int(arg)
            if 1 <= n <= len(threads):
                chosen = threads[n - 1]
            else:
                print(f"Índice {n} fuera de rango (1-{len(threads)})", file=sys.stderr)
                sys.exit(1)
        else:
            # Try to match by ID substring or title
            matches = [t for t in threads if arg.lower() in t['id'].lower() or arg.lower() in t['title'].lower()]
            if not matches:
                print(f"No se encontró ninguna sesión con '{arg}'", file=sys.stderr)
                sys.exit(1)
            chosen = matches[0]
    else:
        choice = interactive_picker(threads)
        chosen = threads[choice - 1]

    print(f"\n>> Retomando: [{chosen['date_str']}] {chosen['title']}")
    print(f"   ID: {chosen['id']}")
    print(f"   Ejecutando: codex resume {chosen['id']}\n")

    subprocess.run(["codex", "resume", chosen['id']], check=False)

if __name__ == "__main__":
    main()
