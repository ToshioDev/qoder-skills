# Image-to-Code Assets

A practical workflow for finding, evaluating, preparing, and handing off visual assets from UI references. Use it alongside the [`image-to-code`](https://github.com/) skill when a reference includes photography, illustrations, mascots, textured artwork, or other meaningful media.

The goal is faithful implementation: reuse approved assets where possible, create only what is missing, keep interface elements editable in code, and give implementation work a precise asset map.

## What it does

- Breaks a reference into sections and components, including supporting shapes and strokes.
- Audits existing project assets and brand identity before creating anything.
- Scores candidate assets for subject, composition, style, palette, and source quality.
- Chooses between reuse, code-native geometry, and generated media based on the reference.
- Creates focused prompts for missing visuals and checks which image tools are actually available.
- Organizes a handoff-ready asset pack with stable names, a manifest, sizing, crop, and placement notes.
- Verifies the result against reference-sized previews and reports fidelity gaps.

## Installation

Install this folder as a Codex skill in your skills directory, preserving its structure:

```text
image-to-code-assets/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
└── references/
    ├── component-audit-and-handoff.md
    └── runtime-and-brand-preflight.md
```

For example, clone this repository into `~/.codex/skills/image-to-code-assets` (Windows: `%USERPROFILE%\.codex\skills\image-to-code-assets`). Restart or refresh Codex if the skill is not detected immediately.

## When to use it

Use this skill when a UI reference contains important image assets or visual media that need to be identified, matched, generated, or handed to an implementation workflow. Pair it with `image-to-code` for full-page analysis and interface implementation.

It is not intended for code-only interfaces, where CSS, SVG, or native components are the right source of truth. It also does not replace structural, responsive, accessibility, or interaction analysis.

## Workflow

1. Decompose the reference into components and classify each visual as media, live UI, a code-native shape, an existing asset, or a mix.
2. Inspect likely asset locations and trace brand, theme, and packaging use to identify canonical files.
3. Compare candidates against the reference using the component audit rubric.
4. Reuse a faithful match, build simple geometry in code, or generate a distinct missing visual.
5. Prepare one focused prompt per missing asset and use only a generation tool available in the current host.
6. Package assets with a manifest that records source, dimensions, aspect ratio, transparency, crop, intended display size, and implementation notes.
7. Hand the exact files and placement guidance to `image-to-code`.
8. Compare the implementation with the reference at matching viewports and correct layout or asset issues based on evidence.

## Core principles

- Treat the supplied reference as the source of truth; do not invent unseen details.
- Search existing assets and source code before creating replacements.
- Preserve approved brand identity and keep separate brands or skins isolated.
- Keep text, controls, and interactive UI live in code.
- Use raster generation for distinctive visual media, not for simple editable geometry or UI.
- Never claim a generated asset is an exact extraction unless the tool and supplied reference support that claim.
- Do not silently add providers, dependencies, paid calls, or external transfers.

## Repository contents

- [`SKILL.md`](SKILL.md): the complete workflow, quality gate, and boundaries.
- [`references/component-audit-and-handoff.md`](references/component-audit-and-handoff.md): evaluation rubric and handoff format.
- [`references/runtime-and-brand-preflight.md`](references/runtime-and-brand-preflight.md): host and brand checks before asset work.
- [`agents/openai.yaml`](agents/openai.yaml): agent-facing metadata.

## License

No license is currently included. Add a license before redistribution if you want to grant reuse permissions; without one, normal copyright restrictions apply.
