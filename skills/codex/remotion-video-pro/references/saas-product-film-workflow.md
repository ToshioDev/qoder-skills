# SaaS product film workflow

Use this reference for launch films, product demos, app explainers, and SaaS commercials. It draws on the public production outline at [Rayyan.pe](https://rayyan.pe/skills/video-saas-premium) and on the local web-builder-pro, image-to-code, image-to-code-assets, and video-editing guidance. This is an adaptable workflow, not a claim to reproduce another creator's private process or guarantee a particular model's output.

## 1. Establish the assignment and evidence

Record the delivery channel, audience, duration, aspect ratio, desired viewer response, CTA, and assets/permissions. Inspect the live product, supplied code or captures, public brand material and relevant customer questions/reviews when accessible. Keep a concise product-dossier.md with each factual statement linked to its source and marked as verified, inferred, or concept-only. Use competitor research to understand category conventions; do not lift their copy, footage, or interface.

Never invent customer quotes, metrics, integrations, product states, or shipped features. If only a URL is available, inspect the real pages and disclose what could not be verified. Prefer the running product or user-provided screenshots over assumptions.

## 2. Develop a brand-specific creative route

Define what the audience should understand, feel, and do. When the direction is open, propose three concepts that differ in cinematic mechanism and visual structure, such as a continuous camera move, a real interface journey, or a meaningful before/after. Recommend one and say why it is specific to this product. Reject any idea that still works unchanged after swapping the logo for a competitor.

Analyze a supplied reference by timed beat: framing, camera, edit rhythm, transition cause, type, UI behavior, sound, holds, and payoff. Explain what is transferable before building. Keep a short history of recent concepts in the project when the user is producing a series; avoid repeating their visual skeleton.

If the user has already chosen a route or explicitly asked you to decide and proceed, honor that instruction. Do not create an approval bottleneck by asking them to reselect known decisions.

## 3. Capture the product faithfully

Collect the key screens and actions that support the story. Inspect screenshot dimensions, viewport, text, typography, spacing, colors, and visible product state. Build an editable UI component map; recreate genuine details from evidence. Mark any deliberately speculative screen as concept UI and keep it from implying a feature is already shipped.

When third-party surfaces appear (messaging, calendar, OS chrome), use accurate proportions and only the visible details the shot needs. Remove or replace personal data only with the user's authorization; don't expose private capture data in public renders. Keep readable UI, logos, text, and controls as code/vector layers. ImageGen is for substantive raster assets and scene plates, not exact UI text or approved marks.

## 4. Lock a visual animatic before full production

Create 6–8 representative keyframes covering the hook, product context, meaningful interaction/state change, payoff, close, and any transition endpoints that affect continuity. For each frame include time/frame, shot scale, camera or viewport, active UI state, graphic hierarchy, safe-area notes, and asset source. Render actual stills at delivery aspect ratio. Correct composition and product fidelity while changes are still cheap.

A keyframe board is not proof of motion. Before polishing, create a short motion prototype or transition strip with start, middle, and end frames. Confirm that UI and product scale, camera path, and scene-to-scene direction remain coherent. Avoid title cards, repeated top labels, and static centered headings unless the concept calls for them.

## 5. Build shots as authored scenes

Make a scene map with exact in/out frames for screen, cursor or touch, device, camera, type, graphic layers, voice, music, and effects. Use a restrained, coherent design language derived from the product, but let each shot earn its own framing. UI pop-outs and feature callouts should emerge from a real product event, attach to the element they describe, and close or resolve before the next beat. Never let them hover as unrelated stickers.

Pick tools for the shot:
- Use GSAP for sequenced UI choreography and camera moves when the timeline can be sought deterministically.
- Use Three.js only where real depth, perspective, reflections, occlusion or a physical device materially improve the shot. Validate camera, lens, scale, materials and shadows together.
- Use Motion-style springs for tactile interactions only if the render path can reproduce the same values for any requested frame.
- Use existing Rive/Lottie animations when their visual style and timing fit the project.
- Use Remotion's frame clock for deterministic React scenes. Use HyperFrames for HTML-first compositions when its child-composition/timeline model and capture path suit the project.

Do not combine all tools by default. No browser wall-clock animation, uncontrolled randomness, or animation that looks different when a frame is rendered out of order. Group each scene's layers so unrelated products, backdrops, UI and sound cannot leak into another scene.

## 6. Make audio part of the edit

Plan voice, music, ambience, silence, foley and effects in the animatic. Match one sound to one meaningful cause: input gets a restrained typing texture, send gets a send cue, arrival gets a distinct receive cue, a physical press gets material-specific foley, and a major camera move may get a designed whoosh. Use silence for thinking/loading beats when it helps comprehension. Avoid constant whooshes and generic UI bloops.

Select commercial-use sound by audition and verify item-level licensing and delivery restrictions; log source, creator, license, download date and intended cue. A music downbeat should support a meaningful edit or spoken idea, not every cut. If using generated voice/music, confirm the provider, license, key/tool availability and user's authorization; otherwise use cleared supplied audio or deliver without generated voice. Keep voice and on-screen copy aligned, and inspect the final mix for clipping, masking and inconsistent levels.

## 7. Inspect motion and polish like an editor

Render preview stills/contact sheets for every scene's opening, middle, closing, and both sides of every cut. Inspect transition midpoint frames, not just attractive endpoints. Then review the rendered clip at normal speed and frame-step scenes with dense motion. Check:

- UI against source captures: text, colors, alignment, states, visible controls and believable interactions.
- Story and pacing: the viewer understands the product, each shot adds information, holds are intentional, and no beat feels like a slide.
- Motion: easing, anticipation, weight, readable entrances, clean exits, no floating layers, collisions, clipping, transform jumps or cuts that reverse screen direction without motivation.
- Visual finish: type hierarchy, image crop, lighting/material consistency, device shape/orientation, focal hierarchy, safe areas, and an intentional close.
- Audio: event sync, transition timing, voice intelligibility, mix levels and silence.
- Delivery: aspect ratio, codec, dimensions, frame rate, duration and file playback.

Fix issues observed in the render and repeat the affected checks. Do not report a visual/audio validation unless the rendered artifact was actually inspected. If time, disk, browser, or tooling prevents a final render, say exactly which checks remain and provide the available preview artifact. Use 4K/60 fps only when requested or justified by delivery and source quality; a larger export does not repair weak art direction or low-detail inputs.
