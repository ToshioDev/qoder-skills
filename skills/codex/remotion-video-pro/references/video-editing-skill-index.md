# Video Editing and Remotion Skill Index

Research snapshot: 2026-10-15. This is a curated index, not an installation list. Official Remotion skills are the baseline for Remotion-specific implementation. Third-party skills are candidates for narrow workflows and should be inspected before use.

## 1. Official Remotion Agent Skills - primary source

Repository: [remotion-dev/skills](https://github.com/remotion-dev/skills)  
Official overview: [Remotion Agent Skills](https://www.remotion.dev/docs/ai/skills)  
The official docs say these skills support Codex and other coding agents. The current official set includes:

| Skill | Use it for |
| --- | --- |
| `remotion-best-practices` | General Remotion work or routing when the right focused skill is unclear. |
| `remotion-create` | New Remotion projects and compositions. |
| `remotion-markup` | React composition structure, frame-based animation, typography, layout, assets, sound, and timing. |
| `remotion-studio` | Starting and previewing Remotion Studio. |
| `remotion-render` | Rendering a video or still. |
| `remotion-captions` | Captions and subtitles. |
| `remotion-interactivity` | Making elements selectable/editable in Studio. |
| `remotion-docs` | Looking up current APIs and package guidance. |
| `remotion-upgrade` | Updating Remotion packages and the official skills together. |
| `remotion-maps` | Maps, routes, markers, and geographic animation. |
| `remotion-saas` | Remotion-backed apps and product integrations. |
| `remotion-multimedia` | Browser-based media metadata with Mediabunny. |

Prefer the focused skill for the task; use `remotion-best-practices` as the fallback. The official documented install route is `npx skills add remotion-dev/skills`; inspect the target and ask before changing the user's global skill setup or project dependencies.

## 2. Official Remotion GSAP integration

- [@remotion/gsap docs](https://www.remotion.dev/docs/gsap)
- [`useGsapTimeline()` API](https://www.remotion.dev/docs/gsap/use-gsap-timeline)

This is a Remotion package/integration rather than an Agent Skill. It synchronizes a paused GSAP timeline to Remotion's current frame. Use it for deterministic, complex React video motion. Its documented restrictions matter: no wall-clock playback/callbacks or free-running tweens, no unseeded randomness, and no GSAP plugins such as ScrollTrigger or Draggable in the rendered composition. Check version compatibility and keep Remotion package versions aligned before installing.

## 3. Existing local design and motion skills

These are present in the current Codex skill catalog; combine selectively with the official Remotion skills:

| Skill | Use it for |
| --- | --- |
| `web-builder-pro` | Premium art direction, anti-slop, product goals, visual references, brand assets, conversion copy, responsive site design. Adapt its design system to video rather than turning the video into a slideshow. |
| `animation-reference-curator` | Finding, inspecting, and rating motion references before design. |
| `web-animation-preview` | Building a motion blueprint or a runnable browser animation preview. Translate browser motion into frame-based video choreography. |
| `web-preview-generator` | Exploring a visual design direction before building. |
| `image-to-code` | Implementing faithfully from a visual reference when image-led design is relevant. |
| `image-to-code-assets` | Analyzing and packaging visual assets from references. |
| `imagegen` | Generating a new raster image or visual asset when useful. |

## 4. Third-party skill candidates

These public repositories describe more specialized video workflows. They are not official Remotion skills and have not been security-audited as part of this index. Review their current code, dependencies, license, and data/network behavior before installing or running them.

- [video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - candidate for cinematic product videos, storyboards, reusable shot/motion recipes, and sound design. Consider when a product promo needs more structured shot planning than the official base skills provide.
- [Claude Remotion Skill](https://github.com/haidrrrry/claude-remotion-skill) - candidate for motion-graphics craft such as staggered typography, captions, color treatment, and sound design. Despite its name, inspect portability and current Remotion practices before using it in Codex.
- [vexjoy-agent video-editing](https://github.com/notque/vexjoy-agent/tree/main/skills/content/video-editing) - candidate for footage-first editing pipelines that separate editorial decisions from deterministic FFmpeg cuts and Remotion composition. Useful when the input is long raw footage rather than a clean motion-graphics brief.
- [remotion-video](https://github.com/techdou/remotion-video) - candidate for subtitle/transcript-led explainer videos that parse SRT, create a storyboard, compose scenes, and render. Check its template and scripts before adoption.

Treat public star counts and promotional claims as weak quality signals. Select a skill based on workflow match, code quality, maintained docs, license, dependency scope, and whether it improves the actual deliverable. Do not combine overlapping video skills by default.

## 5. Rotoscopy and extraction references

- [Remotion `@remotion/video-matting`](https://www.remotion.dev/docs/video-matting) - official local/browser and Node video foreground/background separation. Studio can export a transparent WebM. Requires a supported GPU/WebGPU and compatible video decode plus VP9 alpha encode; check model-specific licenses and device support.
- [Remotion transparent video guidance](https://www.remotion.dev/docs/transparent-videos) - alpha-capable output formats and embedding guidance.
- [Meta SAM 2](https://ai.meta.com/research/sam2/) and [official repository](https://github.com/facebookresearch/sam2) - promptable image/video object segmentation with temporal propagation and corrections. Useful for object-specific roto masks; a mask still needs alpha compositing and edge cleanup.
- [Robust Video Matting (RVM)](https://github.com/PeterL1n/RobustVideoMatting) - candidate for foreground matting of people. Treat it as a human matting method, not a general arbitrary-object segmenter.
- `imagegen` - available for still image edits/cutouts where transparent background generation is appropriate; it does not by itself process an entire video clip.

Use the Remotion package first when its local requirements and edge quality fit. Use SAM 2 for promptable object masks, and human matting models for people. Refine alpha edges and temporal stability in the chosen compositing tool. Preserve original footage; never upload private footage to cloud services without the user's authorization. Verify current model/package versions, hardware requirements, and licenses before installation or production use.
## 6. Route by task

- **Brand promo, product launch, kinetic typography:** official `remotion-best-practices` + `remotion-markup`; optionally `video-shotcraft` as a reviewed reference; `@remotion/gsap` for deterministic GSAP choreography.
- **Edit existing footage with transcript or captions:** official `remotion-captions` plus a reviewed FFmpeg/footage-editing workflow; use Remotion for titles, captions, compositing, and graphics.
- **Map explainer:** official `remotion-maps` and `remotion-markup`.
- **Product demo from a website:** `web-builder-pro` for brand/art direction, capture or inspect the real product UI when authorized, storyboard the journey, then build scenes with Remotion. Do not fabricate UI details.
- **Video delivered inside a website:** use Remotion for the rendered media or React Player where compatible; build the surrounding web page in the existing supported stack. A React Player is React-specific; for Angular or Astro integration, use a rendered video asset or an explicitly supported embedding approach.
## Platform format and trend research

- [TikTok Creative Center](https://ads.tiktok.com/business/creativecenter/quicktok/online/Creating_Made_Easier/pc/en) and [Creative Codes](https://ads.tiktok.com/business/library/Creative_Codes_ENG.pdf)
- [Instagram Best Practices](https://about.fb.com/news/2024/10/best-practices-education-hub-creators-instagram/) and [Reels trends/editing features](https://about.fb.com/news/2023/04/instagram-reels-trending-audio-and-gifts-updates/)
- [YouTube Shorts editing tips](https://support.google.com/youtube/answer/13380879?hl=en), [creation tips](https://support.google.com/youtube/answer/12948448?hl=en), and [Shorts analytics tips](https://support.google.com/youtube/answer/12942217?co=YOUTUBE._YTVideoType%3Dshorts&hl=en)

For current examples, use platform-native trend tools and the relevant creator's own analytics when available. Separate reusable story/edit patterns from fleeting audio/meme trends. These sources do not guarantee virality; note dates and market, and verify audio rights.
