# Visual Assets

Use this reference when deciding whether a README should include an image, GIF, video, diagram, or sample-output block.

## Decision rule

Recommend a visual only when it improves comprehension or trust faster than text alone.
Use [header.md](header.md) for top-of-README images, support badges, contact badges, and hidden improvement comments.

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

- Put a screenshot below `About` when readers need immediate product proof.
- Put a gallery after `Features` when multiple capabilities are easier to understand visually.
- Put a GIF near `Usage` when the value is in the transition, not a single final state.
- Put sample output right after install or run commands when readers need to verify success.
- Put diagrams near architecture only when they reduce cognitive load.

## Format selection

- Use a static image for a single screen, artifact, or state.
- Use a GIF for short silent loops.
- Use a video when the flow is longer, includes audio, or would be too heavy as a GIF.
- Use sample output for CLIs and tooling when the result is primarily textual.

## Existing vs missing assets

When assets exist:

- inspect them
- place them where they reduce uncertainty fastest
- use relative asset paths that resolve correctly from each README location, especially in multilingual `Docs/` layouts
- avoid overloading the README with too many visuals

When assets do not exist:

- do not invent filenames, links, or hosted demos
- recommend the best insertion point
- describe what the asset should show
- state why that placement helps
- name the appropriate format

## Recommendation examples

- Add a product screenshot below `## About` so readers can see the default dashboard before reading the feature list.
- Add a short GIF in `## Usage` that shows the create-edit-save flow because the transition is the key value.
- Add a terminal output example after the launch command so readers can confirm the tool started correctly.
