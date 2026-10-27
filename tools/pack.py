"""Build a portable skills bundle from the local agent skill directories."""

import getpass
import hashlib
import json
import pathlib
import re
import shutil
import zipfile

HOME = pathlib.Path.home()
OUT = HOME / "qoder-skills-portable"
SOURCES = [
    ("qoder", HOME / ".agents" / "skills"),
    ("codex", HOME / ".codex" / "skills"),
    ("claude", HOME / ".claude" / "skills"),
    ("cursor", HOME / ".cursor" / "skills"),
    ("gemini", HOME / ".gemini" / "config" / "skills"),
    ("grok", HOME / ".grok" / "skills"),
]
SKIP_DIRNAMES = {".git", "__pycache__", "node_modules", ".idea"}
SKIP_SUFFIXES = {
    ".pyc", ".pyo", ".so", ".dll", ".png", ".jpg", ".jpeg", ".gif", ".webp",
    ".ico", ".woff", ".woff2", ".ttf", ".zip",
}
TEXT_SUFFIXES = {
    ".md", ".txt", ".json", ".yaml", ".yml", ".csv", ".py", ".js", ".ts",
    ".toml", ".html", ".css", ".sh", ".bat", ".ps1", ".cfg", ".ini",
}

FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

# Applied only to the bundle copy, so a public repo does not leak the local account name.
# Patterns are bytes because blobs are read as bytes; the account name comes from the
# environment so the tool itself is safe to publish. $env:USERPROFILE because the affected
# snippets live in ```powershell fences, where %USERPROFILE% would not expand.
LOCAL_USER = re.escape(getpass.getuser().encode())
REDACTIONS = [
    (re.compile(rb"[A-Za-z]:\\+Users\\+" + LOCAL_USER, re.IGNORECASE), b"$env:USERPROFILE"),
    (re.compile(rb"(?:/c)?/Users/" + LOCAL_USER, re.IGNORECASE), b"$HOME"),
]

# Private strings that must never leave this machine (real session titles, client names).
# Loaded from redactions-local.json, which is gitignored; see redactions-local.example.json.
LOCAL_REDACTIONS_FILE = pathlib.Path(__file__).resolve().parent / "redactions-local.json"
ZIP_EXCLUDE_NAMES = {"redactions-local.json"}
SKILL_REDACTIONS = {}
if LOCAL_REDACTIONS_FILE.is_file():
    raw = json.loads(LOCAL_REDACTIONS_FILE.read_text(encoding="utf-8"))
    for key, rules in raw.items():
        origin, _, skill = key.partition("/")
        SKILL_REDACTIONS[(origin, skill)] = [
            (re.compile(pattern.encode(), re.IGNORECASE), replacement.encode())
            for pattern, replacement in rules
        ]
NAME_RE = re.compile(r"^name:\s*(.+?)\s*$", re.MULTILINE)
DESC_RE = re.compile(r"^description:\s*(.*(?:\n(?:[ \t]+.*|.*))*)", re.MULTILINE)


def flatten(value: str) -> str:
    value = value.strip()
    if value in (">", ">-", "|", "|-"):
        return ""
    return re.sub(r"\s+", " ", value).strip("\"'")


def read_frontmatter(skill_md: pathlib.Path):
    text = skill_md.read_text(encoding="utf-8", errors="replace")
    match = FRONTMATTER.match(text)
    if not match:
        return None, None
    block = match.group(1)
    name = NAME_RE.search(block)
    desc = DESC_RE.search(block)
    return (
        flatten(name.group(1)) if name else None,
        flatten(desc.group(1)) if desc else None,
    )


def main():
    shutil.rmtree(OUT / "skills", ignore_errors=True)
    OUT.mkdir(parents=True, exist_ok=True)

    manifest = {}
    file_count = 0
    for origin, root in SOURCES:
        if not root.is_dir():
            continue
        for folder in sorted(p for p in root.iterdir() if p.is_dir()):
            skill_md = folder / "SKILL.md"
            if not skill_md.is_file():
                continue
            name, desc = read_frontmatter(skill_md)
            target_root = OUT / "skills" / origin / folder.name
            files = {}
            redacted = []
            blobs = {}
            for path in sorted(p for p in folder.rglob("*") if p.is_file()):
                rel = path.relative_to(folder).as_posix()
                if SKIP_DIRNAMES & set(rel.split("/")):
                    continue
                if path.suffix.lower() in SKIP_SUFFIXES:
                    continue
                blob = path.read_bytes()
                keep_text = path.suffix.lower() in TEXT_SUFFIXES
                redid = False
                if keep_text:
                    # Source tree mixes CRLF/LF and trailing newlines; the fences in the
                    # prompt cannot carry that ambiguity, so text is canonicalised here.
                    blob = blob.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
                    blob = blob.rstrip(b"\n") + (b"\n" if blob.strip() else b"")
                    original = blob
                    for pattern, repl in REDACTIONS + SKILL_REDACTIONS.get(
                        (origin, folder.name), []
                    ):
                        blob = pattern.sub(repl, blob)
                    redid = blob != original
                    if redid:
                        redacted.append(rel)
                files[rel] = {
                    "bytes": len(blob),
                    "sha256": hashlib.sha256(blob).hexdigest()[:16],
                    "text": keep_text,
                }
                if keep_text:
                    blobs[rel] = blob
            if not files:
                continue
            known = manifest.get(folder.name)
            if known is not None:
                # Duplicate across hosts: keep the first origin's copy.
                known["origins"].append(origin)
                if files != known["files"]:
                    known["divergent_origins"].append(origin)
                continue
            for rel, blob in blobs.items():
                dest = target_root / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(blob)
                file_count += 1
            manifest[folder.name] = {
                "frontmatter_name": name,
                "description": (desc or "")[:400],
                "origins": [origin],
                "canonical_origin": origin,
                "files": files,
                "divergent_origins": [],
                "redacted": redacted,
            }

    n_redacted = sum(len(e["redacted"]) for e in manifest.values())
    (OUT / "manifest.json").write_text(
        json.dumps(
            {
                "schema": 3,
                "redactions": (
                    "ruta personal del equipo origen sustituida por $env:USERPROFILE (Windows) "
                    "o $HOME; los archivos marcados llevan 'redacted' en su entrada"
                    if n_redacted
                    else "ninguna: las skills fuente ya no contienen rutas de cuenta local"
                ),
                "redacted_file_count": n_redacted,
                "line_endings": "todos los archivos de texto normalizados a LF; los "
                                "originales en la maquina fuente mezclado CRLF/LF",
                "skill_count": len(manifest),
                "text_file_count": file_count,
                "skills": manifest,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
        newline="\n",
    )

    lines = [
        "# Skills bundle",
        "",
        f"{len(manifest)} skills / {file_count} text files.",
        "Texto normalizado a LF. "
        + (
            f"Rutas personales redactadas en {n_redacted} archivo(s) (columna `redacted`)."
            if n_redacted
            else "Sin redacciones: las skills fuente no contienen rutas de cuenta."
        ),
        "Instalar con `INSTALL-QODER-SKILLS.md` (copia de `PROMPT-instalar-skills-qoder.md`).",
        "`pack.py` / `emit_installer.py` / `verify_prompt.py` son el tooling del equipo origen.",
        "",
        "| skill | name | origins | canonical | divergent | redacted | files | KiB |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for key in sorted(manifest):
        e = manifest[key]
        size = sum(f["bytes"] for f in e["files"].values())
        lines.append(
            f"| {key} | {e['frontmatter_name']} | {'+'.join(e['origins'])} "
            f"| {e['canonical_origin']} | {'+'.join(e['divergent_origins']) or '—'} "
            f"| {'+'.join(e['redacted']) or '—'} | {len(e['files'])} | {size/1024:.1f} |"
        )
    (OUT / "MANIFEST.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8", newline="\n"
    )
    for src_name, dest_name in (
        ("PROMPT-instalar-skills-qoder.md", "INSTALL-QODER-SKILLS.md"),
        ("PROMPT-corto-instalar-skills.md", "INSTALL-RAPIDO.md"),
    ):
        prompt_src = HOME / src_name
        if prompt_src.is_file():
            # LF forzado: un prompt con CRLF dejaria cada linea embebida terminada en "\r"
            # y la verificacion byte a byte del instalador fallaria en el destino.
            (OUT / dest_name).write_bytes(prompt_src.read_bytes().replace(b"\r\n", b"\n"))
        else:
            print(f"aviso: aún no existe {src_name}; ejecuta pack.py otra vez")

    zip_path = HOME / "qoder-skills-portable.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for p in sorted(OUT.rglob("*")):
            if not p.is_file():
                continue
            if {"fragments", "__pycache__"} & set(p.relative_to(OUT).parts):
                continue  # source of the prompt / bytecode cache, not needed on the target
            if p.name in ZIP_EXCLUDE_NAMES:
                continue  # private redaction inputs; the bundle ships the result, not the patterns
            zf.write(p, f"{OUT.name}/{p.relative_to(OUT).as_posix()}")

    print(f"skills: {len(manifest)}  text files: {file_count}")
    print(f"folder: {OUT}")
    print(f"zip:    {zip_path}  ({zip_path.stat().st_size/1024/1024:.2f} MiB)")
    print("sin name en frontmatter:", [k for k, v in manifest.items() if not v["frontmatter_name"]])
    print("sin archivos de texto:", [k for k, v in manifest.items() if not any(f['text'] for f in v['files'].values())])


if __name__ == "__main__":
    main()
