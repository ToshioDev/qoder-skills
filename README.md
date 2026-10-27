# qoder-skills

Colección de 29 skills de agente (Qoder / Codex / Claude / Cursor /
Gemini / Grok) para diseño web, UI/UX, reconstrucción de sitios, marca, animación, vídeo
con Remotion, investigación multiplataforma e higiene de texto.

Se instalan pegándole un prompt al agente, no ejecutando un instalador.

## Instalar en otra máquina

1. Descarga el bundle:
   ```bash
   curl -L -o qoder-skills-portable.zip \
     https://github.com/ToshioDev/qoder-skills/raw/main/bundle/qoder-skills-portable.zip
   ```
2. Pega el contenido de `install/PROMPT-corto-instalar-skills.md` en el agente de la otra
   máquina, teniendo el zip en su directorio de trabajo o en `~/Downloads`.
3. El agente detecta las rutas de skills, copia sin pisar lo existente y verifica los 182
   archivos contra `manifest.json` (bytes + sha256). Recarga la sesión para que indexe.

Sin acceso al repo, usa `install/PROMPT-instalar-skills-qoder.md`: trae el texto de 28 de
las 29 skills dentro del propio prompt (800 KiB). `ui-ux-pro-max` es la única que exige el
zip, por tamaño de su dataset.

## Contenido

| ruta | qué es |
| --- | --- |
| `bundle/qoder-skills-portable.zip` | Todo, para `curl` |
| `manifest.json` / `MANIFEST.md` | Inventario con hash por archivo |
| `skills/<origen>/<skill>/` | Las mismas carpetas, sin comprimir, para leer en la web |
| `install/*.md` | Los dos prompts instaladores |
| `tools/` | El pipeline que genera el bundle (`pack.py` → `emit_installer.py` → `verify_prompt.py`) |

| skill | origen | archivos | procedencia |
| --- | --- | --- | --- |
| `01-frontend-design` | qoder | 1 | ⚠ terceros |
| `02-responsive-design` | qoder | 1 | propia |
| `03-web-design-guidelines` | qoder | 1 | ⚠ terceros |
| `04-theme-factory` | qoder | 21 | ⚠ terceros |
| `05-website-rebuild` | qoder | 6 | propia |
| `06-local-business-rebuild` | qoder | 3 | propia |
| `07-azerbaijan-website-build` | qoder | 8 | propia |
| `08-design-system-generator` | qoder | 1 | propia |
| `agent-reach` | qoder | 8 | ⚠ terceros |
| `animation-reference-curator` | codex | 4 | propia |
| `antislop-decks` | qoder | 1 | propia |
| `antislop-docs` | qoder | 1 | propia |
| `antislop-web` | qoder | 1 | propia |
| `brand-visual-assets` | codex | 1 | propia |
| `clean-user-facing-text` | codex | 7 | propia |
| `codex-resume` | gemini | 3 | propia |
| `frontend-design` | qoder | 1 | ⚠ terceros |
| `gpt-taste` | codex | 1 | propia |
| `image-to-code` | codex | 1 | propia |
| `image-to-code-assets` | codex | 5 | propia |
| `import-to-claude-code` | claude | 1 | propia |
| `playwright-cli` | qoder | 11 | propia |
| `remotion-video-pro` | codex | 5 | ⚠ terceros |
| `remove-ai-marks` | codex | 7 | propia |
| `ui-ux-pro-max` | qoder | 73 | ⚠ terceros |
| `web-animation-preview` | codex | 3 | propia |
| `web-builder-pro` | codex | 2 | propia |
| `web-design-guidelines` | codex | 1 | ⚠ terceros |
| `web-preview-generator` | codex | 3 | propia |

## Procedencia y licencias

Lo marcado como **propia** es trabajo mío. Estas provienen de otros proyectos y las
incluyo con atribución, no como declaración de autoría:

- **`01-frontend-design`** — Anthropic skill pack. El frontmatter cita `LICENSE.txt` y ese archivo no está en el bundle: verifica la licencia en el upstream antes de redistribuir.
- **`frontend-design`** — Anthropic skill pack. Igual que `01-frontend-design`; son dos copias con redacción distinta del mismo skill.
- **`04-theme-factory`** — Anthropic skill pack. Cita `LICENSE.txt` sin incluirlo. Revisar upstream.
- **`03-web-design-guidelines`** — Vercel (web-design-guidelines). Frontmatter `author: vercel`, versión 1.0.0.
- **`web-design-guidelines`** — Vercel (web-design-guidelines). Copia sin prefijo numérico de la anterior.
- **`agent-reach`** — Panniantong/Agent-Reach. Skill de terceros con su propio repo y backends configurables.
- **`ui-ux-pro-max`** — dataset agregado. Sin licencia declarada. `data/data-provenance.json` y fichas `*-upstream.json` documentan las fuentes (Google Fonts, Phosphor Icons).
- **`remotion-video-pro`** — remotion-dev/skills. Referencia skills de Remotion en `references/video-editing-skill-index.md`; el resto es trabajo propio.

Antes de republicar o vender nada de esto, verifica las licencias de arriba en su origen.
No incluyo `LICENSE` global por ese motivo.

## Notas de seguridad

- `remove-ai-marks` y `clean-user-facing-text` eliminan marcas de procedencia (Unicode
  invisible, metadatos C2PA/EXIF/XMP, watermarks estadísticos). Pensadas para contenido
  propio; sus propios `references/ethics.md` y `responsible-use.md` prohíben usarlas para
  evadir divulgaciones obligatorias o falsear autoría.
- `05`/`06`/`07` extraen contenido de sitios existentes: confirma tu derecho antes.
- `codex-resume` va atada a la CLI `codex` de OpenAI en Windows.
- Ninguna skill necesita MCP ni introduce credenciales; las que requieren APIs lo declaran
  (`agent-reach`, `playwright-cli`, despliegues de `05`/`07`).

## Rutas personales

Las skills fuente no contienen rutas de cuenta personal ni títulos de sesiones:
las que invocan scripts usan `$env:USERPROFILE` (PowerShell) o `$HOME`, así que
funcionan tal cual en cualquier máquina. `manifest.json → redacted_file_count`
es `0` y la columna `redacted` está vacía en todas las filas.
