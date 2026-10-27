---
name: web-builder-pro
description: Design and build distinctive, premium websites by researching focused visual references and translating them into responsive, accessible frontend implementations. Use for new websites, landing pages, portfolios, or substantial visual redesigns built with React + Vite, Next.js, Angular, or Astro.
metadata:
  short-description: Build premium websites with strong art direction
---

# Web Builder Pro

Create distinctive, usable websites from the user's brief, the project's existing context, and carefully chosen visual references. This skill targets React + Vite, Next.js, Angular, and Astro only. The reference sites are research sources, not code generators or a checklist to apply mechanically.

## Priority 1: Anti-slop and premium craft

This is the governing design rule. Before coding, identify the predictable, generic solution for this category and deliberately move away from it. Build a specific visual point of view that feels commissioned for this brand, audience, and content. A site should feel considered and expensive through composition, typography, image choice, spacing, detail, and interaction quality, not through gratuitous effects or visual noise.

Reject these defaults unless the brief clearly calls for them:

- Generic SaaS landing-page formula: centered headline, gradient blob, logo strip, identical feature cards, testimonial cards, pricing cards, and a final CTA in the same order.
- Bento grids used automatically, repeated card rows, nested boxes, or every section enclosed in a rounded panel.
- Generic AI copy, invented product claims, fake metrics, filler testimonials, fake logos, pseudo-technical labels, empty badges, and ornamental pills.
- Default purple/blue gradients, glass effects, glow, stock imagery, icons, or motion added without a reason tied to the brand or content.
- Repeated section geometry, overused split layouts, cramped typography, huge empty gaps, and decorative complexity that weakens hierarchy.

Use specific, truthful content. If important facts are missing, write restrained copy that does not invent them or ask a focused question when the missing information changes the design. Prefer one memorable, well-executed idea over a pile of fashionable effects. A premium result can be quiet, editorial, playful, technical, or expressive; choose based on the brief rather than equating premium with dark colors, minimalism, or animation.

## Learn the user's design language

Treat the user's supplied references, existing product, written preferences, and corrections as the strongest evidence of their taste. Inspect the current project and any available brand materials before proposing a new visual system. When prior Codex context or memory is available and relevant, use design-specific prompts and feedback to learn the user's working style; keep searches scoped to design work and do not trawl unrelated history. Extract reusable signals such as typography, density, color behavior, image treatment, composition, motion intensity, implementation preferences, and what the user explicitly dislikes.

Apply corrections immediately throughout the current project, not just to the element being discussed. Reuse a preference in later tasks in the same conversation when it still fits. Do not claim to know personal preferences that have not been shown, and do not silently rewrite this skill or persistent memory based on an inferred preference. If the user explicitly asks to save a durable preference, update the relevant authorized project or memory file.

## The user's demonstrated design workflow

The user's past design prompts show a consistent way of working. Apply these as workflow preferences when they fit the request, without copying project-specific business details into unrelated sites:

- Start from the business or product goal and audience. Make the page serve a measurable action such as qualified B2B leads, paid conversions, signups, or product adoption. For commercial pages, investigate named competitors or reference brands when asked, then derive original section ideas and truthful copy from the research.
- Turn a short or iterative prompt into a clear brief. Identify the product, audience, value proposition, desired action, brand assets, reference sites, required sections, platform, and animation ambition. Suggest useful missing sections and ask a few focused questions when the answers will change the direction. Let the user add or remove sections before producing a substantial design preview.
- Do not generate visual drafts at random. First understand the content, brand, and page structure. Then make a coherent preview or art direction. When the user is choosing a direction, guide them toward a design they like through concrete, reviewable iterations.
- Bridge design to implementation. Analyze the chosen preview section by section: layout, copy, type, spacing, colors, image/illustration assets, components, and interaction states. For motion work, make a detailed animation blueprint (trigger, target, sequence, duration/feel, scroll relation, responsive behavior, reduced-motion fallback) that can be passed to frontend implementation.
- Aim beyond a static landing page when the request needs it: include supporting views, footer, forms, pricing, onboarding, or product UI that makes the experience complete. Keep navigation, desktop/mobile behavior, platform differences, and real product actions in view where relevant.
- Treat brand identity as part of the interface. Reuse the actual logo/isotype and derive consistent app icons, web icons, custom illustrations, and signature assets when useful. Do not substitute generic icons or decorative assets for meaningful brand work.
- Make interaction quality deliberate. The user repeatedly asks for advanced but fluid motion (including GSAP, parallax, smooth scroll, 3D, and transitions) when appropriate. Choose techniques supported by the stack, scope, and devices; avoid jank on mobile/PWA, honor reduced motion, and make controls readable and visible before hover.
- Write conversion copy for the actual customer and offer, with no repeated CTA labels, unsupported claims, or redundant text. Commercial pages should feel credible and professional; editorial B2B is a useful direction when it fits the brand, while B2C needs its own voice.
- Iterate against the actual result. Verify that requested changes are visible in the relevant views, fix broken styles and responsive sizing, and refine typography, asset placement, CTA contrast, and transitions. Do not report a visual check that was not performed.

When a user provides only a compact prompt, use this brief scaffold internally and ask only for high-impact gaps:

`Product and offer | Audience | Primary conversion | Brand/assets | Required sections/views | Reference sites | Stack/platforms | Desired motion | Content constraints`

Use the scaffold to improve the prompt into a production-ready design direction, not to force the user to fill in a form. Preserve their conversational style and keep the clarification step quick.
## Workflow

1. **Understand the job.** Identify audience, primary action, content, brand constraints, and whether this is a new build or an existing product. Use React + Vite, Next.js, Angular, or Astro according to the brief and project. Inspect the repository and preserve its established patterns. Do not introduce or recommend a different framework under this skill. Ask only for information that materially affects the outcome and cannot be inferred.
2. **Set an art direction.** For an open-ended design, define a concise point of view, visual hierarchy, and page structure before implementation. Explain the key choice briefly when useful. Avoid assembling unrelated gallery styles into a moodboard-like collage.
3. **Research selectively.** Consult only the sources relevant to this site. Inspect live examples or screenshots when browser or web tools are available. Record what is useful: layout logic, type scale, spacing, materials, content density, interaction, and responsive behavior. Adapt patterns; do not reproduce an entire site or copy protected text and assets.
4. **Build a complete experience.** Implement the direction in the current stack with reusable components, real page content, responsive behavior, and functional interactions. Keep dependencies proportionate. Ensure the visual system carries through navigation, content sections, CTAs, footer, and relevant empty or error states.
5. **Review and refine.** When preview or screenshots are available and relevant, inspect wide and narrow viewports. Fix generic-looking sections, visual inconsistencies, overflow, unreadable text, weak contrast, awkward wrapping, broken interactions, and reduced-motion issues before handoff. Run checks only when requested or required by the task workflow.

## Reference map

- [MotionSites AI](https://motionsites.ai/) - prompts, templates, animated backgrounds, and visual direction, especially for motion-rich or 3D marketing pages. Use for ideation; rewrite prompts for the actual brief and stack.
- [Navbar Gallery](https://www.navbar.gallery/) - static and sticky navigation, dropdowns, mega menus, sidebars, search, announcements, full-screen menus, breadcrumbs, and tabs. Decide information architecture and mobile behavior before building.
- [Footer.design](https://www.footer.design/) - footer compositions and visual treatments. Select content groups based on the site's real navigation and contact needs.
- [CTA.gallery](https://www.cta.gallery/) - CTA examples organized by category, industry, and visual mode. Match hierarchy and copy to the real action; appearance alone does not prove conversion performance.
- [404s.design](https://www.404s.design/) - error-page concepts and tone. Keep a clear recovery path such as home, search, or useful links.
- [Unsection](https://www.unsection.com/) - section examples such as hero, features, testimonials, CTA, footer, blog, navbar, pricing, FAQ, team, contact, and portfolio. Adapt a relevant pattern to the site's own system.
- [BentoGrids](https://bentogrids.com/) - bento and modular grids. Use only when the content benefits from modular grouping; derive visual weight from information priority and make mobile reflow clear.
- [60fps.design](https://60fps.design/) - interaction and motion references including gestures, transitions, effects, and component behavior. Translate only relevant cues into the web platform, including keyboard, touch, and reduced-motion behavior.

Gallery content and availability change. Browse the official source when current examples matter. These are primarily visual reference libraries; do not assume source code, assets, or a specific feature are available unless verified.

## Use available skills and tools

Load relevant installed skills when their workflows fit; do not invoke every skill for every site.

- **Image-led exploration or implementation from a supplied visual:** use `image-to-code` and, when its references matter, `image-to-code-assets`. Follow their image generation and analysis requirements when applicable.
- **Motion direction or a runnable animation prototype:** use `animation-reference-curator` to compare references, or `web-animation-preview` when a preview is requested. Use 60fps.design to ground interaction cues.
- **A site in ChatGPT Sites:** use `sites:sites` for its supported build, preview, and publication workflow. For ordinary repository work, use the project's own tools.
- **A requested UI or accessibility audit:** use `web-design-guidelines`. During implementation, still address obvious accessibility needs.
- **Advanced GSAP direction:** use `gpt-taste` only when the user wants a strongly animated, art-directed approach and the skill is available. Its prescriptive choices remain subordinate to the brief, brand, accessibility, performance, and the user's feedback.
- **Visual preview exploration:** use `web-preview-generator` when the user wants visual directions or design previews before implementation.

Use browser automation and web search only when available and useful. A gallery lookup is not a reason to install dependencies or sign into a service. A named reference site is not automatically an installed integration or callable tool.

## Design and interaction standards

- Make every major section earn its place. Vary density, alignment, scale, and media according to its content while maintaining one coherent design language.
- Treat typography as layout: choose a deliberate type pairing or family, establish a clear scale, tune line lengths and wrapping, and preserve readable body copy.
- Use imagery that has a point of view and supports the content. Preserve supplied brand assets and respect project licenses. Avoid generic stock just to fill space.
- Give primary actions clear labels, destinations, and interaction states. Make secondary actions visibly secondary.
- Treat motion as feedback or storytelling. Prefer efficient properties, avoid blocking scroll, and honor `prefers-reduced-motion`.
- Build responsive navigation intentionally, with semantic controls, keyboard operation, visible focus, and touch-friendly targets.
- Give empty, error, and not-found states a useful next step. A 404 can be expressive while keeping recovery obvious.
- Use semantic HTML, descriptive links, accessible control names, sufficient contrast, and meaningful alt text. Keep text legible over images and gradients.
- Use bento, cards, gradients, blur, 3D, and other visual trends only when they solve a real communication or interaction need.

## Quality gate before handoff

Ask whether the result could be mistaken for an uncustomized template. If yes, refine the art direction, section rhythm, typography, imagery, copy, or details until it reflects the actual project. Also check that the primary action is obvious, content is truthful, mobile behavior is intentional, interactions work, and motion has a reduced-motion path where appropriate.

## Output expectations

Deliver the working implementation in the current project and summarize the chosen direction, key patterns used, main files changed, and verification performed. Mention gallery references that materially informed the design when useful. Do not claim tests, accessibility audits, or browser checks that were not run.
