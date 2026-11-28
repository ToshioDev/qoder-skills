"""End-to-end test of the pasteable installer prompt.

Rebuilds the tree from BLOQUE B exactly like the receiving agent would, writes it to a
temp dir, then runs the manifest verification from the prompt's step 6 against it.
Exits non-zero on any byte difference, so a prompt that ships is a prompt that installs.
"""

import hashlib
import json
import pathlib
import re
import shutil
import sys
import tempfile

HOME = pathlib.Path.home()
PROMPT = HOME / "PROMPT-instalar-skills-qoder.md"
BUNDLE = HOME / "qoder-skills-portable"
DEST = pathlib.Path(tempfile.gettempdir()) / "qoder-skills-roundtrip"

FILE_LINE = re.compile(r"^FILE: (\S+) bytes=(\d+) sha256=([0-9a-f]{16})$")
ZIP_ONLY = {"ui-ux-pro-max"}


def rebuild():
    shutil.rmtree(DEST, ignore_errors=True)
    DEST.mkdir(parents=True)
    lines = PROMPT.read_text(encoding="utf-8").split("\n")
    written = {}
    i = 0
    while i < len(lines):
        m = FILE_LINE.match(lines[i])
        if not m:
            i += 1
            continue
        rel, size, digest = m.group(1), int(m.group(2)), m.group(3)
        open_fence = lines[i + 1]
        if not re.fullmatch(r"~{4,}QODERSKILL", open_fence):
            sys.exit(f"{rel}: la línea FILE no va seguida de una valla de apertura")
        j = i + 2
        body = []
        while j < len(lines) and lines[j] != open_fence:
            body.append(lines[j])
            j += 1
        if j >= len(lines):
            sys.exit(f"{rel}: valla sin cerrar (fin del prompt)")
        blob = ("\n".join(body) + "\n").encode("utf-8")
        if len(blob) != size:
            sys.exit(f"{rel}: el prompt declara {size} bytes y su bloque da {len(blob)}")
        if hashlib.sha256(blob).hexdigest()[:16] != digest:
            sys.exit(f"{rel}: el hash declarado en el prompt no cuadra con su propio bloque")
        dest = DEST / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(blob)
        written[rel] = blob
        i = j + 1
    return written


def main():
    manifest = json.loads((BUNDLE / "manifest.json").read_text(encoding="utf-8"))["skills"]
    written = rebuild()
    print(f"bloques reconstruidos: {len(written)}")

    problems = []
    expected = 0
    for name, entry in sorted(manifest.items()):
        if name in ZIP_ONLY:
            continue
        skill_md = DEST / name / "SKILL.md"
        if not skill_md.is_file():
            problems.append(f"{name}: falta SKILL.md")
        for rel, meta in sorted(entry["files"].items()):
            if not meta["text"]:
                continue
            expected += 1
            rebuilt = written.get(f"{name}/{rel}")
            if rebuilt is None:
                problems.append(f"{name}/{rel}: ausente en el prompt")
                continue
            canonical = BUNDLE / "skills" / entry["canonical_origin"] / name / rel
            if not canonical.is_file():
                problems.append(f"{name}/{rel}: ausente en el bundle")
                continue
            original = canonical.read_bytes()
            if rebuilt != original:
                problems.append(
                    f"{name}/{rel}: {len(rebuilt)} bytes reconstruidos vs {len(original)} en origen"
                    + ("" if rebuilt[:24] != original[:24] else f" | dif: {original[:24]!r}")
                )

    print(f"archivos de texto esperados: {expected}  problemas: {len(problems)}")
    for p in problems[:12]:
        print("  -", p)
    if problems:
        sys.exit(1)
    zip_bytes = (HOME / "qoder-skills-portable.zip").stat().st_size
    total = len(manifest)
    print(
        f"OK: el prompt reconstruye {total - len(ZIP_ONLY)} de {total} skills byte a byte; "
        f"{', '.join(sorted(ZIP_ONLY))} requiere el zip ({zip_bytes/1024/1024:.2f} MiB)"
    )


if __name__ == "__main__":
    main()
