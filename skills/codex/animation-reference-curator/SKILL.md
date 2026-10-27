---
name: animation-reference-curator
description: Find, inspect, rate, and select high-quality animation references for a specific page or app brief. Use when planning motion direction for React/web or Flutter, especially when comparing cinematic scroll, parallax, 3D, Rive, Lottie, or UI animation approaches.
metadata:
  short-description: Curate and rate animation references
---

# Animation Reference Curator

Curate examples that fit the page's purpose, visual direction, platform, and implementation constraints. The output is a scored reference shortlist and a handoff brief for implementation or preview work; this skill does not implement the animation or generate the preview itself.

## Workflow

1. **Read the project first.** Identify the framework, existing animation/rendering packages, page structure, target devices, and design system. Do not assume a new dependency is wanted. If the project is not available, use the brief and state assumptions.
2. **Translate the page brief into motion goals.** Record the audience, brand tone, primary story or action, content hierarchy, desired intensity, interaction model (scroll, pointer, touch, time-based), and constraints. Distinguish the page's needs from visual references that are merely attractive.
3. **Search for candidate references.** Use live search when available. Prefer actual runnable demos and first-party libraries or studios; use curated galleries as discovery indexes. Search separately for visual direction and technically relevant platform examples. For a complex React landing page, include GSAP/ScrollTrigger and React Three Fiber candidates where relevant. For Flutter, consider built-in animations, Rive, Lottie, CustomPainter, shaders, or a suitable 3D runtime according to the requested effect.
4. **Inspect before scoring.** Open each candidate and check the actual motion, controls, mobile behavior where possible, and whether it still runs. Search snippets, thumbnails, and marketing claims are leads, not evidence. If live inspection is unavailable, label the score provisional and state why.
5. **Rate each candidate with the rubric** in [evaluation-and-handoff.md](references/evaluation-and-handoff.md). Score fit to this page, not abstract popularity. Keep visual inspiration and implementation feasibility as separate judgments.
6. **Build a useful candidate set.** Compare several candidates internally, then show the user 2–3 meaningfully different motion directions, not a long gallery dump. Include the score and strongest trade-off for each, and keep a feasible fallback for an ambitious direction.
7. **Get the user's direction before handoff.** Explain what each shortlisted direction would feel like in this page. Ask which one they prefer or what to change; a high score is not user approval. If they ask you to decide, recommend one and mark it as proposed. Once selected, send the handoff fields in [evaluation-and-handoff.md](references/evaluation-and-handoff.md) to implementation/preview collaborators.
8. **Maintain a catalog only when useful.** If the user asks for a persistent catalog, or the project already has one, add or update entries in the project-selected location. Keep source, inspection date, platform, score, confidence, and license/usage status. Do not silently create a catalog in a system or global directory.

## Guide the design decision

Help the user react to concrete visual and motion choices instead of asking them to invent technical specifications. Describe the page outcome in plain language and offer a small number of distinct options. Ask one focused question at a time. Accept feedback such as "too fast", "less game-like", or "more cinematic" and translate it into specific changes. Preserve choices they approved; do not make them re-approve the same direction after each refinement. Continue until they approve, ask to stop, or request implementation. The user decides what feels right; ratings support the decision but never replace it.
## Platform routing

- **React/web:** Follow the existing stack. CSS or the Web Animations API can be enough for simple transitions. Consider Motion for component/UI motion, GSAP with ScrollTrigger for choreographed and scroll-scrubbed timelines, and Three.js/React Three Fiber for real-time 3D scenes. Use Rive or Lottie for authored graphics when they fit. Do not prescribe smooth-scroll hijacking; assess native scroll and reduced-motion behavior.
- **Flutter:** Prefer Flutter's built-in animation system for widget and route transitions. Consider Rive for interactive state-driven vector animation, Lottie for authored After Effects sequences, CustomPainter or shaders for bespoke 2D effects, and a 3D runtime only when the project requires it. Do not imply that a Rive/Lottie clip is equivalent to a scroll-driven WebGL scene.
- **Unknown framework or platform:** Ask only for missing information that materially changes the shortlist. Otherwise provide separate platform-specific feasibility notes.

## Output

Start with the motion concept in plain language. Then provide the ranked references with links and short evidence-based reasons. End with a compact handoff brief. Do not call a reference “best” without explaining its relevance to this page. Avoid recommending a library solely because it appears in a demo.

Read [gallery-sources.md](references/gallery-sources.md) when you need starting points for live examples. Recheck sources during each task; galleries and library APIs change.
