# PROMPT: instalar mi colección de skills en otra instancia de Qoder

Pega TODO este archivo en el agente Qoder del otro ordenador. No necesita internet.
Bloque A te dice de dónde tomar los archivos, BLOQUE B los contiene ya escritos.
Actúas como instalador: recreas la colección exacta, detectas en qué carpetas viven las
skills en ESA máquina, las registras y verificas que el host las ve. No inventes skills,
no reescribas redacciones, no "mejores" nada: copia los bytes tal cual.

## Catálogo ({{SKILL_COUNT}} skills)

Origen `qoder` = `~/.agents/skills` (también espejadas en `~/.claude/skills`).
Origen `codex` = `~/.codex/skills`. Las demás columnas salen de `manifest.json`.

{{CATALOGUE}}

Conviven dos parejas casi idénticas a propósito: `03-web-design-guidelines` /
`web-design-guidelines` y `01-frontend-design` / `frontend-design`. El prefijo numérico
existe para que no choquen en el índice de skills. Conserva ambas carpetas salvo que el
usuario pida una sola; en ese caso elimina la variante sin prefijo.

`codex-resume` es la única casada a este equipo: invoca la CLI `codex` de Windows para
retomar sesiones. Si en el destino no existe, dilo y no la instales.

## BLOQUE A — cómo obtener los bytes

Sigue este orden y detente en el primero que funcione:

1. **Zip adjunto (recomendado, y obligatorio para `ui-ux-pro-max`).** Busca
   `qoder-skills-portable.zip` en el directorio de trabajo, `~/Downloads` o el escritorio.
   Descomprime (crea una carpeta raíz propia) y usa ESOS archivos como fuente de verdad:
   ```
   qoder-skills-portable/
     manifest.json              # skill -> origen canónico, archivos, bytes, sha256(16)
     MANIFEST.md                # misma tabla legible, con columna `divergent`
     INSTALL-QODER-SKILLS.md    # copia de este prompt (autocontenido, skills embebidas)
     INSTALL-RAPIDO.md          # versión corta, exige el zip
     pack.py emit_installer.py verify_prompt.py   # tooling del equipo origen
     skills/qoder/<skill>/...   # copias exactas de ~/.agents/skills  (canónicas)
     skills/codex/<skill>/...   # copias exactas de ~/.codex/skills
     skills/<otro>/<skill>/...  # solo lo que NO existe en un origen anterior
     ```
   El manifest trae `text_file_count: {{TEXT_FILE_COUNT}}` (archivos únicos; los espejos
   duplicados entre `~/.agents` y `~/.claude` se descartan y solo se anotan en
   `divergent_origins`).
   Contrasta skill por skill con
   `files[<ruta>] = {bytes, sha256, text}`. Los archivos de texto están normalizados a LF y
   con un único salto de línea final, así que el hash no va a coincidir con tu copia local
   desordenada: coincide con la del bundle. Cualquier discrepancia contra el bundle: para,
   informa, no instales a medias.

2. **Sin zip: recrea desde el BLOQUE B**, que trae todas las skills excepto
   `ui-ux-pro-max`. Cada bloque empieza con una línea `FILE: <ruta/relativa>`.

3. **Ninguna de las dos**: da al usuario los comandos de origen y vuelve cuando haya
   paquete. Origen (Windows + Git Bash):
   `python "$HOME/qoder-skills-portable/pack.py"` → produce `~/qoder-skills-portable.zip`;
   transferir con `scp ~/qoder-skills-portable.zip usuario@otra-maquina:~/Downloads/`.
