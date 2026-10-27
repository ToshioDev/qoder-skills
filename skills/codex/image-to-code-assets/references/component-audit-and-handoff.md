# Component asset audit and handoff

Use this when the input is a screenshot, generated design, product mockup, or multi-component reference. It turns visual inspection into an actionable extraction package for the `image-to-code` implementation.

## 1. Walk the reference

Break the page into sections and components, then inspect each component's internal visual elements. Where resolution permits, record the source image dimensions and each asset's bounding box as pixel coordinates and normalized fractions `(x, y, width, height)` of its parent. For responsive references, keep a row per viewport rather than inferring mobile behavior from desktop.

For each visible item, record:

| Field | Record |
|---|---|
| Component / item | Stable name matching the UI structure |
| Evidence | What is visibly present; note uncertain details explicitly |
| Role and type | Photo, illustration, mascot, logo, icon, texture, data graphic, geometric shape, organic silhouette, stroke/linework, live UI, or mixed |
| Bounds | Reference viewport, parent, approximate x/y/w/h, and alignment |
| Display treatment | Aspect ratio, crop/focal point, background, transparency, borders/shadow only if intrinsic to the asset |
| Decision | Reuse exact file, adapt crop/scale, generate new, build in code, or ask/unknown |
| Asset path | Existing canonical location or planned output filename |
| Handoff notes | Render size, fit, theme variant, accessibility role, responsive behavior |

Separate intrinsic asset appearance from CSS framing. A rounded screenshot frame or card border may belong to the component, not the source image. A UI preview can be mixed: preserve all readable text, buttons, and controls as real code, extracting only the embedded photograph/illustration.

### Supporting shapes, strokes, and objects

Alongside photos and illustrations, make a deliberate pass for small but identity-bearing/supporting forms: organic blobs, cutout silhouettes, sketched strokes, underlines, hand-drawn circles, arrows/connectors, rays, sparkles, paper/document shapes, waveforms, patterns, glows, and compact objects placed around a card or heading. Note which are present in the reference and how they relate to adjacent content. Search the site's existing image/vector assets and implementation (SVG, CSS, canvas, icon sets, component libraries) for a faithful reusable match before creating anything.

Choose implementation by observed shape complexity:

- Use CSS or inline SVG for basic geometry and controllable UI strokes (rules, borders, circles, rounded rectangles, arrows, simple charts/diagrams, icons, and predictable decorative geometry).
- Reuse the site's existing image/SVG if the silhouette, line character, palette, and scale fit the reference.
- Use ImageGen for distinct organic/irregular silhouettes, expressive hand-drawn linework, painterly or textured forms, and meaningful supporting objects whose specific appearance cannot be reproduced faithfully with the available assets or concise code.
- Keep these as separate assets from text and controls. Do not bake UI copy, card frames, or interaction states into the generated artwork. Do not generate an asset merely to approximate a basic CSS shape, and do not omit a distinctive visible trace because it seems “just decorative.”

When a mark or trace is too small/unclear to classify, record the uncertainty and compare a reference crop at larger scale; do not invent its shape or silently replace it with a generic sparkle/blob.

## 2. Evaluate existing files

Inspect candidate visuals—not just filenames—including intrinsic pixel size, aspect ratio, color/alpha, transparent padding, and appearance over the intended background. Verify actual use through source/config references and active theme/brand selection.

Use a quick 0–2 fit score for each dimension (maximum 10):

1. subject/identity;
2. composition, silhouette, pose, and focal point;
3. style, medium, linework, or rendering;
4. palette and material;
5. source quality for the target size, aspect/crop, and transparency.

Treat `8–10` as a likely reuse candidate, `5–7` as requiring deliberate crop/adaptation or comparison with a new generation, and `0–4` as a mismatch. These are review bands, not an automatic decision. A canonical approved logo is reused in its correct background/theme variant even if superficial screenshot antialiasing differs; do not replace brand identity by score.

## 3. Write a prompt from evidence

For each missing raster candidate, crop/zoom the reference for analysis when useful; retain the full reference for surrounding context. Build a separate prompt from observed properties:

- content identity and exact object/character count;
- pose, view/camera angle, silhouette, and relative arrangement;
- medium/material, edge/line quality, palette, and shading;
- composition, margins/negative space, and visual center;
- intended transparent or solid background and target aspect ratio;
- the target component's rendered size and contrast context;
- explicit exclusions for unrelated UI, lettering, borders, or extra objects.

Use reference-image conditioning where supported and appropriate. Keep distinctive motifs and character identity faithful; “same style” alone is not a sufficient prompt. Do not claim pixel-level extraction from a generator: verify the generated result against the reference, and reuse/crop the original asset when exact identity matters and reuse is authorized.

## 4. Package outputs

Prefer a dedicated staging folder such as:

```text
design-assets/<reference-name>/
  asset-map.md
  images/
    feature-audio-transcript.png
    feature-topic-materials.png
```

Follow repository conventions if they are clearer. `asset-map.md` should carry the audit table and concise generation/source notes. The image files must be present in the workspace—not generator-cache paths. Do not duplicate canonical existing project files solely to make the staging folder appear complete; map their real path in the manifest. Keep original reference images intact and preserve existing files.

## 5. Handoff payload for image-to-code

Give the implementer:

1. the full design reference(s) and viewport dimensions;
2. the asset map/folder and exact canonical paths;
3. component-to-file mapping and observed bounding boxes;
4. intended display aspect/size, crop/focal point, background, and responsive behavior;
5. which parts remain live frontend (text, buttons, controls, lists, charts/diagrams where appropriate);
6. unresolved details and confidence—never silently fill them with invented design.

During implementation, size assets from their reference bounds and keep natural aspect ratio unless visible evidence shows a crop. Verify the result using matching viewport screenshots and side-by-side/overlay comparison; tune component layout, CSS `object-fit`/`object-position`, and spacing to match. Do not stretch the bitmap to compensate for a wrong layout.
