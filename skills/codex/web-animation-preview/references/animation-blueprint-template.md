# Animation Blueprint

## Handoff metadata

- Page/project:
- Static design preview path(s):
- Blueprint status: proposed / approved / implemented
- Target platform/framework:
- Project/repository inspected: yes / no
- Previously stated motion preferences:

## Evidence and motion direction

- Purpose and intended feeling:
- Intensity:
- Input model: native scroll / pointer / touch / state / time
- Observed visual cues:
- Inferred affordances:
- Proposed motion:
- Unknowns requiring source files or user input:

## Component and asset inventory

Repeat for each animated or interactive element. Describe a buildable abstraction without assuming a particular framework.

### <stable-id> — <visible component/asset>

- Section and semantic role:
- Evidence/status: observed / inferred / proposed; proposed / approved / rejected
- Source image region or visual anchor:
- Component type: DOM / SVG / raster / 3D mesh / canvas / video / unknown
- Parent → child hierarchy / scene-graph node names:
- Static visual construction: silhouette, shape, geometry, proportions, stroke, spacing, and repeated variants:
- Bounds and placement: use normalized ratios relative to the section/image when exact pixels are unknown:
- Origin/pivot and coordinate axes, if applicable:
- Layer/depth order:
- Material, color, surface, light, shadow, and camera/framing:
- Current state and required states:
- Animatable properties:
- Interactive states and keyboard/touch requirements:
- Source asset availability/license/status:
- Missing source or production replacement:

## Section storyboard

Repeat for each meaningful beat. Values are explicit proposals unless marked approved.

### <Section> — <beat name>

- Target component IDs:
- Purpose:
- Trigger and trigger boundaries:
- Initial state:
- Keyframes: time/progress → property values (include units or normalized values):
- Duration or scroll span:
- Easing/physics:
- Layering/depth relationship:
- Exit/next state:
- Desktop behavior:
- Mobile/touch behavior:
- Keyboard behavior:
- Reduced-motion/static fallback:
- Performance/visibility constraints:
- Status: proposed / approved / rejected

## Detailed asset/model prompts

Provide a ready-to-use prompt for each new visual asset or model. Name the intended generator/tool or mark it tool-agnostic. Never claim an image generator can return rigged geometry unless that tool supports it.

### <asset-id> — <deliverable type>

```text
Intended use:
Deliverable type and format:
Subject and purpose:
Geometry / silhouette / exact object count:
Object hierarchy and stable mesh/layer names:
Proportions and shared origin/pivot:
Coordinate system and desired separability:
Camera / framing / aspect ratio:
Materials / surface / color:
Lighting / shadows:
Background / transparency:
Animation-ready requirements:
Must preserve:
Avoid:
```

## Implementation route

- Preferred approach after repository inspection:
- Existing packages to check:
- DOM/SVG/CSS/2D/3D object mapping:
- No-install fallback:
- Performance considerations:
- Do not animate as a flattened raster:

## Image-to-code handoff

- Static design image remains the source of truth for layout, copy, typography, color, component geometry, and assets.
- This blueprint is the source of truth for approved motion behavior and animation-ready component/asset abstractions.
- Pass the static preview path and this blueprint path to the coding skill.
- Implement approved beats. Get direction on proposed beats that materially change the experience.
- Preserve native scrolling, responsive behavior, content visibility without motion, and reduced-motion fallback.
- Keep prototype controls out of production unless requested.
- Additional source assets needed:
- Unresolved questions:

## Prompt for the coding skill

```text
Use the static design preview at <preview path> as the visual source of truth and read <blueprint path> before coding. Reconstruct the named component and asset hierarchy; do not animate the flattened preview image. Implement the approved animation tracks and preserve all provisional/rejected statuses. Inspect the existing project and dependencies before selecting libraries. Follow the documented geometry, proportions, origins, materials, keyframes, breakpoints, accessibility, and reduced-motion fallbacks. Do not invent copy, assets, product claims, or motion beyond this contract. List any unresolved item rather than guessing.
```
