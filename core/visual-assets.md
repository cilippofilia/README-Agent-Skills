# Visual Assets

Use this reference when deciding whether a README should include an image, GIF, video, diagram, or sample-output block.

## Decision rule

Recommend a visual only when it improves comprehension or trust faster than text alone.
Support badges are not treated as decorative visuals. Include them by default when the repo explicitly states supported versions.

Good reasons:

- the reader needs to see what the product looks like
- the workflow includes meaningful state changes
- a successful result is easier to recognize visually
- a concept is too dense in prose and simpler as a diagram

Bad reasons:

- decoration
- filling space
- repeating information the text already explains well

## Placement heuristics

- If a README includes a logo, pill, or brand mark near the top, place it on its own line above the `# Title`.
- Do not place logo or pill images inline inside the H1 heading unless the user explicitly asks for that layout.
- When a repo has a polished logo, wordmark, or brand image asset, recommend a centered image block above the title rather than starting with plain text.
- If the repo targets Apple platforms or other clearly defined runtimes, include a compact badge row near the top for verified OS and language support.
- If the repo has an obvious maintainer contact channel, recommend a matching top-of-README contact badge only when the handle or URL can be verified from the repo or user input.
- Put a screenshot below `About` when readers need immediate product proof.
- Put a gallery after `Features` when multiple capabilities are easier to understand visually.
- Put a GIF near `Usage` when the value is in the transition, not a single final state.
- Put sample output right after install or run commands when readers need to verify success.
- Put diagrams near architecture only when they reduce cognitive load.

## Top-of-README composition

For product-style READMEs, this order usually works well when the assets and metadata are available:

1. centered logo or hero image block
2. compact support and ecosystem badges
3. `# Title`
4. one-sentence value proposition

Prefer this top block when it improves trust or recognition quickly. Skip any element that cannot be verified.

## Badge sourcing

Treat support badges as default README metadata when the evidence is explicit. Sources can include:

- `Package.swift` platform declarations
- Xcode project or workspace deployment targets
- `.xcodeproj` and `.xcconfig` build settings
- CI matrices or tested-version docs
- tool manifests such as `.swift-version`, `mise.toml`, or language-specific config files

Infer support badges only from clear source-of-truth files. Do not guess versions from APIs, imports, or vague prose.

## Format selection

- Use a static image for a single screen, artifact, or state.
- Use a GIF for short silent loops.
- Use a video when the flow is longer, includes audio, or would be too heavy as a GIF.
- Use sample output for CLIs and tooling when the result is primarily textual.

## Existing vs missing assets

When assets exist:

- inspect them
- place them where they reduce uncertainty fastest
- avoid overloading the top of the README with too many visuals
- use relative asset paths that resolve correctly from each README location, especially in multilingual `Docs/` layouts
- keep top badges factual and minimal rather than turning the header into a wall of metadata
- prefer the smallest verified badge set that answers "what does this run on?" immediately

When assets do not exist:

- do not invent filenames, links, or hosted demos
- recommend the best insertion point
- describe what the asset should show
- state why that placement helps
- name the appropriate format
- if the README is being generated or rewritten directly, add a nearby hidden comment using `[//]: # (...)` to preserve that recommendation in the file

## Recommendation examples

- Add a centered brand image block above `# ScreenPrivacy`, then place iOS, macOS, Swift, and contact badges directly under it so the README communicates identity and support before the body copy.
- Add the package pill on its own line above `# ScreenPrivacy` rather than inline in the heading so the title stays clean and portable across renderers.
- Add a product screenshot below `## About` so readers can see the default dashboard before reading the feature list.
- Add a short GIF in `## Usage` that shows the create-edit-save flow because the transition is the key value.
- Add a terminal output example after the launch command so readers can confirm the tool started correctly.
- `[//]: # (Hero section: this would benefit from a centered image above the title, for example <p align="center"><img src="Docs/Images/hero.svg" alt="Project logo" width="60%" /></p>)`
- `[//]: # (Usage section: this would really benefit from a short video or GIF example of the feature in action.)`
