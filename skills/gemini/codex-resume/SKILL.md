---
name: codex-resume
description: >-
  Usa esta skill cuando el usuario escriba /resume, "resume codex", "retomar codex",
  "abrir chat de codex", "ver mis chats de codex" o cualquier variante.
  Muestra el listado de sesiones del perfil default de OpenAI Codex (excluyendo
  sesiones de AlphaAI) y permite elegir una para retomar con `codex resume`.
  También acepta un número o fragmento del título como argumento directo.
---

# Skill: codex-resume

Esta skill lista y permite retomar sesiones del perfil **default** de OpenAI Codex
directamente desde AGY, filtrando automáticamente las sesiones de AlphaAI.

## Cuándo activar

Activar cuando el usuario diga:
- `/resume`
- "resume codex" / "retomar codex"
- "ver mis chats de codex"
- "abre el chat de codex número X"
- "continúa el chat de [nombre]"
- "mis sesiones de codex"

## Pasos

### Opción A — Picker interactivo (sin argumentos)

Ejecuta el script sin argumentos para mostrar el menú completo:

```powershell
python "$env:USERPROFILE\.gemini\config\skills\codex-resume\scripts\codex_resume.py"
```

El script:
1. Lee `~/.codex/thread_history_1.sqlite` y `~/.codex/session_index.jsonl`
2. Filtra sesiones de AlphaAI detectando menciones de `alphaai`, `qwen`, `cloudflare`, etc.
3. Muestra un listado numerado de las sesiones default ordenadas por fecha (más reciente primero)
4. El usuario elige un número
5. Lanza `codex resume <id>` automáticamente

### Opción B — Resume directo por número o nombre

Si el usuario ya sabe qué chat quiere (ej: "el chat 39" o "el de facturas"):

```powershell
# Por número
python "$env:USERPROFILE\.gemini\config\skills\codex-resume\scripts\codex_resume.py" 39

# Por fragmento de título
python "$env:USERPROFILE\.gemini\config\skills\codex-resume\scripts\codex_resume.py" "facturas"
python "$env:USERPROFILE\.gemini\config\skills\codex-resume\scripts\codex_resume.py" "web"
```

### Opción C — Desde esta conversación en AGY

Si el usuario no quiere abrir Codex nativo y prefiere continuar aquí en AGY:
1. Lee el archivo exportado correspondiente en `$env:USERPROFILE\codex_exported_chats\`
2. Carga el contexto del proyecto (archivos modificados, prompts anteriores)
3. Continúa el trabajo directamente desde AGY

## Notas

- La base de datos es `~/.codex/thread_history_1.sqlite` (>1.5 GB, no modificar)
- Las sesiones de AlphaAI se detectan por texto en los mensajes del agente (menciones a Qwen, Alibaba, cloudflare, alphaai, pulselat)
- El script [codex_resume.py](./scripts/codex_resume.py) es de solo lectura sobre la BD de Codex
- El wrapper [codex_resume.bat](./scripts/codex_resume.bat) permite llamar el script desde cmd/pwsh sin prefijo python
