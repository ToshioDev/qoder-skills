# Codex runtime and brand preflight

Read this reference when a task depends on Codex-specific image generation or a repository contains several logos, themes, product skins, or competing asset variants. Recheck product documentation when behavior may have changed.

## Brand inventory: establish what is already real

1. List assets in likely locations (`assets/`, `public/`, platform bundles, brand/theme folders); identify image dimensions, formats, transparency, and duplicates where useful.
2. Search references to candidate paths in application code, theme/profile selectors, manifests, metadata, README/docs, and build/package configuration. The currently wired asset and its selection logic are stronger evidence than the filename.
3. View the actual likely marks and illustrations. Confirm legibility on their intended backgrounds and any light/dark variants. A transparent white mark can look blank on a white viewer; preview it on a contrasting background.
4. Record canonical asset by role and context (for example, generic product logo vs founder skin; light header vs dark footer). Reuse the right variant; do not “clean up” unused historical files unless asked.
5. If source/configuration and rendered behavior disagree, or two identities look equally active, report the evidence and ask before replacing or rebranding. Do not let assets from one skin/persona appear in another without an explicit design requirement.

## Generation capability: session-scoped, not assumed

- Inspect the tools available in this exact Codex session and whether the local `imagegen` skill is available. A tool used earlier or in another Codex installation does not prove current availability.
- When the built-in image-generation tool is exposed, the `imagegen` skill is the workflow for raster generation/editing. Use that native route by default; keep generated files in the project and inspect them.
- If it is absent, stay with existing project media or code-native SVG/CSS when they meet the need. If raster generation is essential, tell the user generation is unavailable in this session and ask which provider/tool to connect. Do not silently install, configure, authenticate, or route to an outside service.
- A user-selected external generator must be available through an explicitly configured, trusted tool integration (often MCP, if supported by the selected Codex surface). Confirm provider identity, authentication scope, data handling, and cost before sending source images or prompts. Never assume a random MCP server is an image provider just because it exposes tools.
- Keep separate facts separate: Codex can connect to MCP servers that expose tools; an image-generation API is another integration/credential/billing path. Neither fact proves that a given Codex session has a particular provider or that a ChatGPT/Codex subscription includes API calls. Do not improvise undocumented endpoints or API-key/CLI fallbacks.

## Portability across agent CLIs

The procedural `SKILL.md` and reference files are deliberately host-neutral. Claude and Gemini CLI both document Agent Skills using a `SKILL.md` directory format, but installation paths, discovery, metadata extensions, permissions, and tool availability are host-specific. Do not copy Codex's `agents/openai.yaml` and assume it configures another host. Check that host's current skill list and MCP/tool inventory first; use an image tool only if the current host exposes it or the user has configured a trusted generator. MCP availability means a server is connected, not that it has image generation.

- [Claude Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) and [Claude Code MCP](https://docs.anthropic.com/en/docs/claude-code/mcp)
- [Gemini CLI Agent Skills](https://geminicli.com/docs/cli/using-agent-skills/) and [Gemini CLI tools/MCP](https://geminicli.com/docs/reference/tools/)

OpenAI product docs (recheck for current behavior):

- [Codex skills](https://developers.openai.com/api/docs/guides/tools-skills) — skills package reusable instructions and supporting resources; they are not a guarantee that a tool is installed.
- [Connectors and MCP servers](https://developers.openai.com/api/docs/guides/tools-connectors-mcp) and [Docs MCP](https://developers.openai.com/learn/docs-mcp) — Codex surfaces can connect MCP tools; review trust and data access for third-party servers.
- [Plugin quickstart](https://developers.openai.com/plugins/quickstart) — a plugin can bundle a skill, MCP server, or both. This is a way to package/connect capabilities, not proof of an image generator being present.
- [Image generation tool](https://developers.openai.com/api/docs/guides/tools-image-generation) — the OpenAI API's image-generation tool is an API integration; do not conflate it with a native Codex session tool or infer subscription entitlements from its existence.

The current skill metadata format documents MCP as the supported declared tool dependency type; it does not declare one skill as a hard dependency of another. Therefore this skill describes a logical handoff to `imagegen` and checks its availability at runtime instead of pretending it can install or require it automatically.
