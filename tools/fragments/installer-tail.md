## BLOQUE C — skills que solo viajan en el zip

{{ZIP_ONLY_LIST}}
  No se pueden recrear desde texto en un prompt. Si no tienes el zip, instálalas en cuanto
  lo tengas y dilo en el informe; NO escribas un dataset simulado ni recortes
  "representativos": `scripts/` hace consultas sobre esos datos y un dataset parcial da
  respuestas falsas con apariencia de verdad.

Reglas ya aplicadas al empaquetar: fuera `.git/`, `__pycache__/`, `*.pyc` y binarios
(imágenes, fuentes, `.zip`). El resto viaja tal cual, LF y un único salto de línea final.
`agents/openai.yaml` sí se incluye: es configuración de un host Codex concreto; para Qoder
es ruido inerte y puedes borrarlo si el usuario quiere un árbol limpio (dilo en el informe).

## Pasos de instalación

### 1. Detecta las rutas de skills del receptor

No asumas. Enumera y decide con lo que exista:

```bash
for d in "$HOME/.agents/skills" "$HOME/.qoder/skills" "$HOME/.claude/skills" \
         "$HOME/.codex/skills" "$HOME/.cursor/skills" "$HOME/.config/qoder/skills" \
         "./.qoder/skills" "./.agents/skills" "./skills"; do
  [ -d "$d" ] && echo "EXISTE: $d"
done
```

- El directorio canónico para Qoder en esta configuración de origen es `~/.agents/skills`
  (Qoder lo indexa directamente, igual que `~/.claude/skills`).
- Si en la máquina destino **no existe ninguno**, crea `~/.agents/skills` y úsalo.
- Proyecto (`.qoder/skills` o `.agents/skills` junto al repo) solo si el usuario pide
  instalación por proyecto. Por defecto: global.
- Si hay varios candidatos, instala en el canónico y ofrece el espejo después; no dupliques
  sin avisar. Pregunta una sola vez, con la lista detectada, y sigue.

### 2. Copia sin destruir lo que ya hay

```bash
SKILLS_DIR="$HOME/.agents/skills"        # sustituye por la ruta detectada
SRC="/tmp/qoder-skills-portable/skills"  # o donde descomprimiste
mkdir -p "$SKILLS_DIR"
for o in qoder codex claude; do
  [ -d "$SRC/$o" ] || continue
  for f in "$SRC/$o"/*/; do cp -rn "$f" "$SKILLS_DIR/"; done
done
```

`cp -rn` (no-clobber) es deliberado: si destino ya tiene una skill con ese nombre, se
conserva la del usuario. Lista esos choques en el informe y espera instrucción — nunca
sobrescribas una skill existente por tu cuenta.

### 3. Normaliza solo lo que el host exija

- **Finales de línea:** el paquete está normalizado a LF (el árbol de origen mezclaba
  CRLF/LF, por eso `manifest.json` documenta `line_endings`). Escribe los archivos con LF
  y sin transformar; si tu entorno convierte a CRLF al grabar, el hash del paso 6 fallará
  aunque el contenido sea correcto.
- Nombre de carpeta = nombre de skill para el índice. Si `name:` en el frontmatter no casa
  con la carpeta y el host no la lista, renombra la carpeta al valor de `name:` (añadiendo
  el prefijo numérico si eso evita una colisión), no al revés.
- Todo `SKILL.md` debe tener frontmatter YAML con `name` y `description`. Ya lo tienen; si
  algún archivo editado a mano lo pierde, repáralo y muestra el diff.
- No toques el resto del cuerpo.

### 3b. Cadenas específicas de host: reporta, no reescribas a ciegas

Los espejos en `~/.claude/skills` y `~/.agents/skills` no son idénticos: alguien sustituyó
`Claude` ↔ `Codex` en los cuerpos. El paquete lleva la versión de `~/.agents/skills` como
canónica y marca en `manifest.json` (`divergent_origins`) las skills donde el espejo difiere
(`01-frontend-design`, `ui-ux-pro-max`).

Dentro de los cuerpos hay rutas que NO existirán en la máquina destino. Trátalas así:

- **Funcional (hay que arreglarlo y decir qué hiciste):** `ui-ux-pro-max/SKILL.md` invoca
  `python "${CLAUDE_PLUGIN_ROOT}/.Codex/skills/ui-ux-pro-max/scripts/search.py" …`.
  `${CLAUDE_PLUGIN_ROOT}` es una variable de plugin de Claude; fuera de ese contexto se
  resuelve vacío y la ruta queda muerta. Sustitúyela por la ruta absoluta real donde
  instalaste la skill (`$SKILLS_DIR/ui-ux-pro-max/scripts/search.py`) en TODO el archivo,
  muestra el diff y prueba el comando antes de terminar.
{{REDACTION_NOTE}}
- **Cosmético (reporta, deja intacto salvo que el usuario pida lo contrario):** menciones a
  "Codex", "Claude", "Cursor" como destinatario de la skill — p. ej. `image-to-code`
  ("Elite website image-to-code skill for Codex"), `clean-user-facing-text` ("Use in Cursor
  when…"), `gpt-taste` y `01-frontend-design` ("Remember: Codex is capable of…"). Cambiar
  esas palabras por "el agente" es opcional y no afecta a la ejecución; no reescribas
  instrucciones de fondo disfrazando un renombre.
- Busca otras cadenas de ruta antes de cerrar:
  `grep -rn 'CLAUDE_PLUGIN_ROOT\|\.Codex/skills\|\.claude/skills' "$SKILLS_DIR"`.

### 4. Rutas y dependencias internas

- Referencias dentro de una skill (`references/*.md`, `scripts/*.py`) son relativas a la
  carpeta de la skill: se mantienen al copiar la carpeta entera. Verifica en el paso 6.
- Dependencias externas por skill — instálalas solo si el usuario acepta:
  - `playwright-cli`: CLI de Playwright / `npx playwright`.
  - `05`, `06`, `07`: Node + Astro + Tailwind, y `gh`/Vercel CLI para los despliegues.
  - `remotion-video-pro`: Node + Remotion + `ffmpeg`.
  - `agent-reach`: su CLI/backend según canal; sin backend configurado varios canales fallan.
- Dependencias cruzadas reales: `image-to-code-assets` → `image-to-code`;
  `web-animation-preview` → `animation-reference-curator`; `06` reutiliza reglas de `05`;
  `05`/`06`/`07` comparten `references/design-rules.md` y `accessibility-spec.md` (copias
  independientes, intencional). Instala las parejas juntas o la referencia se queda coja.

### 5. Configura el entorno del host destino

Ninguna de estas skills necesita MCP ni claves propias salvo `agent-reach` y `playwright-cli`
(herramientas de navegador) y `05`/`07` (GitHub/Vercel si el usuario quiere desplegar). No
escribas credenciales en las skills ni en `settings.json`.

### 6. Verificación

Contrasta contra `manifest.json` (schema 2: `skills[<nombre>].files[<ruta>]` con `bytes` y
`sha256` de 16 hex). El manifest describe lo que hay **dentro del bundle**, no tu árbol
`~/.agents`/`~/.codex` de origen: allí los archivos que mezclaban CRLF o terminaban sin
salto de línea difieren de la copia del bundle. Es normal.

`python <verificador.py> <ruta-del-manifest> <ruta-de-skills>`:

```bash
python - "$SRC/../manifest.json" "$SKILLS_DIR" <<'PY'
import hashlib, json, pathlib, re, sys
mf = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))["skills"]
root = pathlib.Path(sys.argv[2])            # = la ruta que elegiste en el paso 1
bad = []
for name, entry in sorted(mf.items()):
    folder = root/name
    md = folder/"SKILL.md"
    if not md.is_file():
        bad.append(f"{name}: falta SKILL.md"); continue
    head = md.read_text(encoding="utf-8", errors="replace")[:4000]
    if not re.search(r"^---\s*\n.*?^name:", head, re.S|re.M):
        bad.append(f"{name}: frontmatter sin name")
    for rel, meta in sorted(entry["files"].items()):
        if not meta["text"]:
            continue
        p = folder/rel
        if not p.is_file():
            bad.append(f"{name}: falta {rel}"); continue
        blob = p.read_bytes()
        if len(blob) != meta["bytes"] or hashlib.sha256(blob).hexdigest()[:16] != meta["sha256"]:
            bad.append(f"{name}: {rel} no cuadra ({len(blob)} vs {meta['bytes']} bytes)")
print(f"{len(mf)} skills, {len(bad)} problemas")
for b in bad: print("  -", b)
PY
```

Con el zip, espera `0 problemas`. Instalando solo desde el BLOQUE B, aparecerán los
{{ZIP_ONLY_FILES}} archivos de las skills `no (zip)` del catálogo como `falta ...`: es el
único hueco previsto, y esas skills no se instalan a medias. Un hash que no cuadra en
`scripts/*.py` o `data/*.csv` es grave: la skill dará consejos falsos con apariencia de
verdad; no la dejes instalada sin avisar.

Además: recarga la sesión del agente (las skills se indexan al arrancar), confirma que
aparecen en el listado de skills disponibles, y prueba una invocación real por familia —
p. ej. `/08-design-system-generator` para una marca ficticia y una consulta de búsqueda de
`ui-ux-pro-max` — antes de declarar éxito.

### 7. Informe final

Entrega: ruta elegida y por qué, skills instaladas / omitidas por conflicto, dependencias
no instaladas, resultado de la verificación del paso 6, y qué hay que hacer para que el host
las vea (normalmente reiniciar). Añade la línea de seguridad de abajo, literal.

## Notas de seguridad que el instalador debe enunciar

Tres skills hacen cosas que solo son legítimas con autorización sobre el contenido:

- `remove-ai-marks` y `clean-user-facing-text` eliminan marcas de procedencia (Unicode
  invisible, metadatos C2PA/EXIF/XMP, watermarks estadísticos). Úsalas solo sobre texto o
  archivos del propio usuario o donde esté permitido; **nunca** para evadir obligaciones de
  divulgación ni falsear autoría académica, legal o de prensa. Sus propios archivos
  (`references/ethics.md`, `references/responsible-use.md`) imponen ese límite; no lo
  relajes.
- `05`/`06`/`07` extraen contenido de sitios existentes. Verifica que hay derecho a hacerlo
  antes de reconstruir, y no copies marcas registradas ni fotos ajenas.
- `agent-reach` consulta plataformas con CLIs/APIs de terceros: revisa los términos de cada
  plataforma; no automatices acciones de escritura (publicar, comentar, valorar).

Instalar una skill no le da permiso a nada: son instrucciones, y siguen sujetas a tu
política y a la del usuario.
