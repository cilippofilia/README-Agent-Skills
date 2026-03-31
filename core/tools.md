# Tool READMEs

Use this reference for CLIs, generators, scripts, automation, internal tools, and operational utilities.

## Priorities

1. Explain inputs, outputs, and workflow clearly.
2. Get the reader to a successful run fast.
3. Show what success looks like with sample output when possible.
4. Document assumptions, flags, and operational notes without clutter.

## Recommended section order

- Title
- About
- Requirements
- Installation or Setup
- Usage
- Sample output or result
- Operational notes
- Project Structure, if useful

## What good tool READMEs do

- State the exact job the tool performs.
- Clarify who should run it and in what context.
- Include runnable commands.
- Show expected output, files created, or resulting state.
- Keep operational warnings close to the commands they affect.
- Put verified runtime or platform support near the top when the repo makes it explicit.
- Prefer code blocks and sample output over decorative visuals.

## Visual guidance

For tools, prefer textual proof first:

- terminal output blocks
- generated file examples
- before-and-after snippets

Use GIFs or videos only when interaction, progress, or a UI state change is central to understanding the tool.

Use [header.md](header.md) for badges, contact metadata, and hidden comments near the top. Use [visual-assets.md](visual-assets.md) when deciding between output blocks and non-header media.

## Common mistakes

- Describing the tool vaguely instead of naming inputs and outputs
- Omitting environment assumptions
- Hiding success criteria after long prose
- Using screenshots when terminal output would be clearer
- Writing operational notes too far from the relevant commands
