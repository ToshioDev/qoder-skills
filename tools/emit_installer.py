"""Emit a self-contained, pasteable installer prompt from the bundle.

Every text file is embedded between fences so the receiving agent can rebuild the tree
with no network access. Only the oversized dataset skill stays zip-only.
"""

import hashlib
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from pack import TEXT_SUFFIXES  # same definition as the bundle, or hashes will disagree

HOME = pathlib.Path.home()
BUNDLE = HOME / "qoder-skills-portable"
BUNDLE_META = json.loads((BUNDLE / "manifest.json").read_text(encoding="utf-8"))
MANIFEST = BUNDLE_META["skills"]

FRAG = BUNDLE / "fragments"
ZIP_ONLY = {"ui-ux-pro-max"}
SKIP_DIRNAMES = {".git", "__pycache__", "node_modules"}


def fence_tick(content: str) -> str:
    longest = max((len(m.group()) for m in re.finditer(r"~+", content)), default=0)
    return "~" * max(4, longest + 1) + "QODERSKILL"


def catalogue_table(manifest, notes, zip_only):
    missing = sorted(set(manifest) - set(notes))
    extra = sorted(set(notes) - set(manifest))
    if missing or extra:
        raise SystemExit(
            f"catalogue-notes.json desalineado: faltan {missing}, sobran {extra}"
        )
    rows = [
        "| skill | origen | archivos | KiB | embebida | qué hace |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for key in sorted(manifest):
        e = manifest[key]
        size = sum(f["bytes"] for f in e["files"].values())
        origins = "+".join(e["origins"])
        if e["divergent_origins"]:
            origins += f" (≠ {','.join(e['divergent_origins'])})"
        inline = "no (zip)" if key in zip_only else "sí"
        rows.append(
            f"| `{key}` | {origins} | {len(e['files'])} | {size/1024:.1f} | {inline} "
            f"| {notes[key]} |"
        )
    return "\n".join(rows)


def fill_counts(body):
    files = sum(
        1
        for key in ZIP_ONLY
        for meta in MANIFEST[key]["files"].values()
        if meta["text"]
    )
    return body.replace("{{ZIP_ONLY_FILES}}", str(files))


def zip_only_list(manifest, zip_only):
    lines = []
    for key in sorted(zip_only):
        entry = manifest[key]
        files = entry["files"]
        kinds = {}
        for rel, meta in files.items():
            kinds[rel.rsplit(".", 1)[-1]] = kinds.get(rel.rsplit(".", 1)[-1], 0) + 1
        size = sum(f["bytes"] for f in files.values()) / 1024 / 1024
        breakdown = ", ".join(f"{n} {k}" for k, n in sorted(kinds.items(), key=lambda x: -x[1]))
        lines.append(
            f"- `{key}` — {len(files)} archivos, {size:.1f} MiB ({breakdown})."
        )
    return "\n".join(lines)


def redaction_note(manifest):
    marked = sorted(k for k, entry in manifest.items() if entry["redacted"])
    if marked:
        note = (
            "- **Redactado (hay que rellenarlo):** el paquete no contiene rutas del equipo que "
            "lo generó. Donde las hubo pone `$env:USERPROFILE` (PowerShell) o `$HOME`; las "
            f"skills marcadas son {', '.join(f'`{k}`' for k in marked)} (ver "
            "`manifest.json → skills[<nombre>].redacted`). Sustituye el placeholder por la ruta "
            "donde instalaste la skill, no por la que te dé la gana: "
            '`python "$SKILLS_DIR/codex-resume/scripts/codex_resume.py"`.\n'
        )
    else:
        note = (
            "- **Rutas:** el paquete no contiene rutas de ninguna cuenta personal; las skills "
            "que invocan scripts ya usan formas portables (`$env:USERPROFILE` en PowerShell, "
            "`$HOME` en Unix), así que no hay placeholders que rellenar.\n"
        )
    return note + (
            "  `codex-resume` sí trae una dependencia externa: la CLI `codex` de OpenAI y "
            "sesiones locales que leer. Si en el destino `codex` no está en el PATH, dilo "
            "expresamente y no la des por instalada."
    )


def build_short(head, tail_raw, zip_only_names, skill_count):
    catalogue_free = head.split("## BLOQUE A")[0].split("\n", 2)[2]
    catalogue_free = catalogue_free.replace(
        "Bloque A te dice de dónde tomar los archivos, BLOQUE B los contiene ya escritos.",
        "Necesita `qoder-skills-portable.zip` al lado; sin zip no hay instalación posible.",
    )
    acquire = head.split("## BLOQUE A")[1].split("2. **Sin zip")[0].replace(
        "1. **Zip adjunto (recomendado, y obligatorio para `ui-ux-pro-max`).**",
        "1. **Zip adjunto.**",
    )
    short_sentence = (
        "Instalando solo desde el BLOQUE B, aparecerán los\n{{ZIP_ONLY_FILES}} archivos de "
        "las skills `no (zip)` del catálogo como `falta ...`: es el\núnico hueco previsto, y "
        "esas skills no se instalan a medias."
    )
    replacement = (
        "Sin el zip, esas skills quedan enteras como `falta ...`: no las instales a "
        "medias ni simules su dataset."
    )
    if short_sentence not in tail_raw:
        raise SystemExit("build_short: la frase del BLOQUE B no casa con installer-tail.md")
    body = (
        tail_raw.replace(
            "## BLOQUE C — skills que solo viajan en el zip",
            "## Único hueco conocido: skills que solo viajan en el zip",
        )
        .replace(short_sentence, replacement)
        .replace("{{ZIP_ONLY_LIST}}", zip_only_list(MANIFEST, zip_only_names))
    )
    body = fill_counts(body.replace("{{REDACTION_NOTE}}", redaction_note(MANIFEST)))
    return (
        f"# INSTALADOR RÁPIDO — {skill_count} skills (requiere qoder-skills-portable.zip)\n\n"
        + catalogue_free
        + "\n"
        + acquire
        + "\n2. **No hay zip:** no improvises. Pide `PROMPT-instalar-skills-qoder.md` (trae "
        "las skills embebidas en el propio texto) o los comandos de origen del punto anterior.\n\n"
        + body
    )


def main():
    notes = json.loads((FRAG / "catalogue-notes.json").read_text(encoding="utf-8"))
    head = (FRAG / "installer-head.md").read_text(encoding="utf-8")
    head = (
        head.replace("{{SKILL_COUNT}}", str(len(MANIFEST)))
        .replace("{{TEXT_FILE_COUNT}}", str(BUNDLE_META["text_file_count"]))
        .replace("{{CATALOGUE}}", catalogue_table(MANIFEST, notes, ZIP_ONLY))
    )
    parts = [head]
    parts.append("## BLOQUE B — cuerpo de las skills\n")
    parts.append(
        "Formato: línea `FILE: <ruta/dentro-de-la-skill> bytes=<N> sha256=<16 hex>` y a "
        "continuación el archivo literal entre dos vallas `~~~...QODERSKILL` idénticas entre "
        "sí; ningún archivo contiene esa marca, así que el cierre no es ambiguo. "
        "`bytes`/`sha256` corresponden a UTF-8 con LF y un único salto de línea final. "
        "Recrea cada carpeta completa bajo la ruta detectada en el paso 1 y verifica tamaño "
        "y hash archivo por archivo antes de pasar al siguiente. No cambies ni una palabra.\n"
    )

    chars = 0
    count = 0
    for key in sorted(MANIFEST):
        entry = MANIFEST[key]
        if key in ZIP_ONLY:
            continue
        folder = BUNDLE / "skills" / entry["canonical_origin"] / key
        if not folder.is_dir():
            raise SystemExit(f"missing {folder}")
        others = [o for o in entry["origins"] if o != entry["canonical_origin"]]
        note = f" | también en {','.join(others)}" if others else ""
        if entry["divergent_origins"]:
            note += f" | LA COPIA DE {','.join(entry['divergent_origins'])} DIFIERE"
        parts.append(f"### SKILL `{key}` — origen {entry['canonical_origin']}{note}\n")
        for p in sorted(f for f in folder.rglob("*") if f.is_file()):
            rel = p.relative_to(folder).as_posix()
            if SKIP_DIRNAMES & set(rel.split("/")):
                continue
            if p.suffix.lower() not in TEXT_SUFFIXES:
                parts.append(f"FILE: {key}/{rel}  (binario: solo desde el zip)")
                continue
            content = p.read_text(encoding="utf-8", errors="replace").rstrip("\n")
            tick = fence_tick(content)
            blob = (content + "\n").encode("utf-8")
            digest = hashlib.sha256(blob).hexdigest()[:16]
            parts.append(f"FILE: {key}/{rel} bytes={len(blob)} sha256={digest}")
            parts.append(tick)
            parts.append(content)
            parts.append(tick)
            chars += len(content) + len(rel) + 32
            count += 1
        parts.append("")

    tail_raw = (FRAG / "installer-tail.md").read_text(encoding="utf-8")
    tail = fill_counts(tail_raw).replace(
        "{{ZIP_ONLY_LIST}}", zip_only_list(MANIFEST, ZIP_ONLY)
    ).replace("{{REDACTION_NOTE}}", redaction_note(MANIFEST))
    parts.append(tail)

    dest = HOME / "PROMPT-instalar-skills-qoder.md"
    text = "\n".join(parts)
    dest.write_text(text, encoding="utf-8")

    short = build_short(head, tail_raw, ZIP_ONLY, len(MANIFEST))
    short_dest = HOME / "PROMPT-corto-instalar-skills.md"
    short_dest.write_text(short, encoding="utf-8")

    zip_bytes = (HOME / "qoder-skills-portable.zip").stat().st_size
    print(f"skills inline: {len(MANIFEST) - len(ZIP_ONLY)}  files embedded: {count}")
    print(f"prompt: {dest}  ({len(text)/1024:.0f} KiB, ~{len(text)/4/1000:.0f}k tokens)")
    print(f"prompt corto: {short_dest}  ({len(short)/1024:.1f} KiB)")
    print(f"zip: {zip_bytes/1024/1024:.2f} MiB")


if __name__ == "__main__":
    main()
