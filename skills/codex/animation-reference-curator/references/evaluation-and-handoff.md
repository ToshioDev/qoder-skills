# Evaluation rubric and handoff

## Rating rubric

Rate each candidate from 1 to 5 on every dimension. A score of 3 means suitable/credible, 5 means exceptional for this page, and 1 means a poor fit. Give a one-sentence evidence note for each rating. Weighted total is `sum(rating / 5 * weight)` out of 100.

| Dimension | Weight | What to judge |
|---|---:|---|
| Context and brand fit | 25 | Does the motion reinforce the page's audience, tone, product, and content? |
| Narrative and choreography | 20 | Does movement guide attention or build a coherent sequence rather than add noise? |
| Craft and visual quality | 15 | Are timing, easing, layering, transitions, typography, depth, and finish convincing? |
| Platform feasibility | 15 | Can the current platform and project stack reproduce the important behavior without an unsuitable rewrite? |
| Performance and responsive behavior | 10 | Does it remain smooth and legible on target devices, with sensible fallbacks for reduced capability? |
| Accessibility and user control | 10 | Can users understand and control motion; does the implementation support reduced motion, keyboard/focus, and non-motion access to content? |
| Evidence and usage clarity | 5 | Is the demo live and inspectable, and are source/asset usage rights or limits clear? |

Do not add an extra popularity score. Rate the *reference* and the *implementation fit* separately in the notes. If evidence is missing, do not award the highest evidence score; lower confidence rather than inventing a fact. Mark whether inspection was live, code-based, video-only, or snippet-only.

## Recommendation bands

- **85–100:** strong candidate; verify implementation constraints before committing.
- **70–84:** useful reference; adapt its strongest principle.
- **50–69:** partial inspiration only.
- **Below 50:** omit unless the user specifically asks to study it.

The total is a decision aid, not a promise of quality. A very ambitious reference can score highly as visual direction and poorly as implementation feasibility.

## Candidate record

Use these fields for each candidate. Keep entries concise and link directly to the demo and, if available, its source or official documentation.

```text
Name:
Live demo:
Source / docs:
Platform and technique:
Motion pattern:
Inspection: live | source inspected | video-only | snippet-only
Page fit (1-5): evidence
Choreography (1-5): evidence
Craft (1-5): evidence
Feasibility (1-5): evidence
Performance (1-5): evidence
Accessibility (1-5): evidence
Evidence/usage (1-5): evidence
Weighted total: /100
Confidence: high | medium | low
Borrow:
Adapt or avoid:
Fallback:
Inspected on:
```

## Handoff contract

Pass these fields to implementation/preview collaborators. Preserve the ranked references and provenance; do not reduce the handoff to a mood adjective.

```yaml
page_context:
  purpose: ""
  audience: ""
  visual_direction: ""
  primary_action: ""
  user_preferences: []
  platform: "react-web | flutter | unknown"
  existing_stack: []
  target_devices: []
decision_status: "proposed | selected | approved | revise"
selected_direction: ""
selected_preview_images: []
rejected_or_revise_notes: []
motion_direction:
  intensity: "subtle | expressive | cinematic"
  story_beats:
    - id: ""
      trigger: "scroll | pointer | touch | state | time"
      visual_change: ""
      duration_or_scroll_span: ""
      easing_or_physics: ""
  reduced_motion_behavior: ""
  fallback_behavior: ""
references:
  - name: ""
    url: ""
    score: 0
    confidence: "high | medium | low"
    technique: ""
    borrow: ""
    avoid: ""
implementation_notes:
  preferred_existing_technology: ""
  new_dependency_needed: false
  risks: []
asset_needs: []
preview_requirements:
  route_or_entry: ""
  controls: ["replay", "scrub", "reduced-motion toggle"]
  inspect_at: ["desktop", "mobile"]
```

## Collaboration boundaries

- **Image-to-code and image-to-code-assets:** supply the scored motion references, visual principles to borrow, and any asset needs. Do not treat an animation screenshot as sufficient implementation evidence; separate static art direction from timing and interaction.
- **Web preview generator:** provide the page context, selected direction, intended route/entry point, and asset needs.
- **Web animation preview skill:** provide ordered story beats, triggers, timing, scrub/replay controls, reduced-motion behavior, and the references to compare against.
- This skill selects and explains references. A companion skill owns storyboard previews and step-by-step animation previews; the implementation workflow owns production code. Only invoke those collaborators when available or explicitly requested.
