# Image-derived landing-page visual specification

Keep this record next to the original ImageGen prompt/spec. It documents what the preview visibly contains so later edits preserve the chosen design.

## Preview record

- **Image:** path or conversation image reference
- **Viewport/frame:** observed dimensions/orientation; note if unknown
- **Original prompt/spec:** link or verbatim text
- **Inspection confidence:** high / medium / low

## Page-level observations

- **Overall visual direction:** observed cues (not just mood labels)
- **Visible section order:** list only sections present in the image
- **Sections implied by the brief but not shown:** list separately; do not infer their design
- **Global system:** palette, typography, grid, spacing rhythm, imagery, recurring shapes
- **Responsive evidence:** observed only if multiple viewports are shown; otherwise mark unverified

## Section-by-section record

Repeat for each visible section:

### [Section name or position]

- **Purpose/content:** visible headline, supporting text, CTA, data, and content hierarchy; quote legible copy exactly
- **Components:** navigation, buttons, cards, forms, media, badges, and other distinct parts
- **Composition:** columns, alignment, relative scale, positioning, whitespace, and crop
- **Typography:** hierarchy, approximate scale/weight, line breaks, and contrast
- **Color/material:** observed colors, backgrounds, borders, shadows, texture, and gradients
- **Imagery/assets:** subject, framing, treatment, and relationship to the UI
- **Motion cues:** only what the still implies (e.g. layered depth, direction, scroll cue); do not claim motion was observed
- **Observed vs inferred:** label assumptions and low-confidence details

## Iteration prompt scaffold

Use the original request and image as the baseline. Specify one coherent user-requested change and list invariants:

```text
Edit the provided landing-page design preview.
Keep unchanged: [approved layout, content, brand, and details].
Change only: [the user's requested visual changes].
Preserve the visible sections, component positions, hierarchy, and exact approved copy unless explicitly changed.
Target viewport: [known viewport].
Do not add: [unsupported product facts, extra sections, or unrequested UI].
```

After every edit, update only the affected observations and retain the source prompt and approved invariants.
