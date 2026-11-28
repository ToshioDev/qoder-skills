---
name: web-animation-preview
description: Derive a section-by-section motion blueprint from a static web design preview, or prototype and refine web animations in a runnable preview when requested. Use for React landing-page scroll narratives, parallax, pinned scenes, typography choreography, pointer-driven perspective, and 3D.
metadata:
  short-description: Prototype and refine web motion with the user
---

# Web Animation Preview

Help the user derive and refine motion from an approved visual design. Support two distinct outcomes: a saved motion blueprint from a static preview, or a small runnable prototype when the user asks to see motion live. Make timing and interaction reviewable in prototype mode, gather feedback in plain language, and refine. This skill owns motion analysis and runnable motion prototypes; `web-preview-generator` owns ImageGen-based product-design previews and whole-page visual direction.

## Workflow

1. **Read the approved design context.** Inspect the page, current code, installed dependencies, target devices, and the user's feedback. If an `animation-reference-curator` handoff exists, honor its recorded status: preserve approved choices as fixed; treat proposed choices as revisable; and do not ask the user to reselect an already selected direction. Use scored references as evidence, not commands. Use the selected ImageGen mockup/design contract as the visual source while experimenting with movement; do not replace the design with an unrelated coded preview.
2. **Resolve the motion brief.** Identify what the movement should communicate, what the user sees first, how the story progresses, the intended intensity, and input mode (native scroll, pointer, touch, state, or time). Ask only about a material unknown. If motion direction is still open, offer 2–3 distinct directions with concise comparisons and visual evidence (a live reference or small motion sketch when feasible); avoid asking again when the page preview already established the desired motion. Let the user choose before a costly or invasive prototype; if they ask you to decide, recommend one and mark it as proposed.
3. **Storyboard the sequence.** Break motion into named beats. For each, specify trigger, visual change, timing or scroll span, easing/physics, layering/depth, exit/next state, mobile adaptation, and reduced-motion fallback. Keep narrative, static design, and implementation technique distinct.
4. **Choose the implementation route from the actual project.** Reuse installed tools first. For React, consider native CSS/Web Animations for simple motion, Motion for component interactions, GSAP/ScrollTrigger for choreographed or scrubbed timelines, and React Three Fiber/Three.js for real-time 3D. Use authored Rive/Lottie assets where that is the right medium. Do not use GSAP merely because it is available. If the selected direction needs a new package or external asset, show that need and a no-install/fallback option before adding it.
5. **Build a contained preview.** Implement the smallest representative slice that proves the chosen movement. Keep it separate from production behavior, preserve the user's app and design files, and record files/dependencies changed. Where feasible, include preview-only controls for replay, pause, timeline/scroll scrubbing, intensity, and reduced motion. Controls used to inspect a prototype are not automatically part of the final landing page.
6. **Inspect real behavior.** Run the preview and inspect desktop and narrow/mobile widths. Check scroll/pin boundaries, pointer and touch behavior, keyboard access, reduced motion, content visibility without animation, and rendering/performance risks. Do not claim a scene is smooth or accessible without observing it; list any unverified conditions.
7. **Guide a focused review.** Give the user the route and identify the exact beats to try. Ask a compact feedback question in plain language about rhythm, intensity, depth, legibility, and what felt wrong/right; offer a few clear choices when that makes feedback easier. Accept natural-language reactions; translate them into changes without making the user specify easing curves or implementation details.
8. **Refine and preserve choices.** Change one coherent motion dimension at a time when that makes feedback easier to judge. Keep accepted choices fixed, show the revised preview, and continue until the user approves or asks to stop. If two requests conflict, offer a clear choice with the consequence of each.
9. **Hand off the approved motion.** Record final story beats, timings, triggers, breakpoints, asset needs, reduced-motion/fallback behavior, and implementation notes in a saved `animation-blueprint.md` using the blueprint template. Send its path with the static preview to `image-to-code`/`image-to-code-assets` when implementation is requested. Keep preview-only controls out of production unless requested.

## Static preview to motion blueprint

Use this mode when the user asks to plan, describe, blueprint, or prepare animations from a static website preview and has not asked for a live/runnable demo.

1. Inspect the selected full-page or section design image and record its path. Treat the image as static evidence: identify sections, visual anchors, depth cues, controls, and repeated brand motifs. A still image does not prove that anything is animated.
2. Separate each note as **observed** (visible in the image), **inferred** (likely interaction affordance, such as carousel arrows), or **proposed** (motion design recommendation). Preserve any previously stated motion preference. Never present proposed movement as already approved or already present in the image.
3. Create an implementation-facing abstraction for every selected section, not only a mood description. Inventory the DOM components, visual assets, layers, and model/object hierarchies to animate; define stable names, parent/child structure, geometry and normalized proportions, bounds, origins/pivots, axes, depth order, materials, lighting, and static/animated states where visible or proposed. Then specify animation tracks with trigger, initial/final values, keyframes, units, duration or scroll range, easing, exit state, desktop/mobile/touch/keyboard behavior, and reduced-motion fallback. Label image evidence as observed, inferred, or proposed; mark unknown measurements instead of inventing precision. Use [the blueprint template](references/animation-blueprint-template.md).
4. For each asset that must be generated, sourced, or rebuilt, include a detailed copy/paste production prompt in the blueprint. State intended output type, subject, geometry, scene/object separation and names, proportions, pivot/origin, camera/framing, materials, lighting, palette, background, deliverable format, and must-keep/must-avoid constraints. For code-bound model prompts, ask for separate named objects and animation-ready pivots; never imply a still-image generator can deliver a rigged model. Choose implementation routes only as candidates until the project is inspected. Prefer native scroll with scroll-linked transforms; do not hijack scroll. For true 3D, do not animate a flattened ImageGen raster: use actual geometry/DOM layers or a project-supported 3D asset/runtime. Record a simpler fallback.
5. Save the result as `animation-blueprint.md` in the user's project or chosen handoff directory. If no project directory is available, save it alongside the selected preview image. Use [the blueprint template](references/animation-blueprint-template.md). Include the static preview path and the status of each motion decision.
6. Include a concise implementation handoff for `image-to-code`: treat the selected static preview as the source for layout and the blueprint as the behavior contract; preserve the approved design and copy; implement only approved motion, or present proposed motion for review first. Do not write production code in blueprint-only mode.

## Live prototype mode

Use this mode only when the user asks to see or test the animation live, or requests a runnable prototype. Inspect the actual project and dependencies, then implement a contained preview of the selected beats. Do not add dependencies without checking the project and presenting a no-install fallback where feasible. If a blueprint exists, use it as the motion contract and retain its observed/inferred/proposed/approved statuses. Prototype controls are preview-only unless the user asks for them in production.
## Motion constraints

- Respect native scroll and do not hijack it by default. For scroll-linked timelines, make the relationship understandable and avoid pinning that traps content or breaks mobile flow.
- Prefer transforms and opacity for continuous movement when appropriate; profile complex filters, large canvases, video frames, and large numbers of animated elements.
- Keep text/content readable if animation fails, is disabled, or has not yet started. Honor `prefers-reduced-motion`; replace large spatial movement with a restrained fade or immediate state where appropriate.
- For 3D, define a static/mobile or reduced-capability fallback and keep essential information available in normal document flow.
- Do not copy reference code/assets without checking license and compatibility. A visual reference is not a license or an implementation spec.
- Do not declare user satisfaction from technical correctness. The user decides whether the motion feels right.

## Review response

At each checkpoint, state: what is ready to preview, which feedback you applied, what is still provisional, and the next choice only if a choice is needed. Do not overwhelm the user with a full animation-engine report.
