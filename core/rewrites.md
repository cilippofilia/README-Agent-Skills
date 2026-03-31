# Rewrite Checklist

Use this reference when improving an existing README instead of drafting from scratch.

## Rewrite workflow

1. Preserve factual content that is still correct.
2. Remove stale, vague, duplicated, or generic text.
3. Reorder sections for scanability and momentum.
4. Tighten copy so it sounds intentional rather than templated.
5. Re-check every claim against the repository.
6. Check whether visuals or sample output should be added or recommended.
7. Add hidden improvement comments only where a missing asset or proof materially hurts clarity or trust.

## Typical rewrite fixes

- Move quick start higher for packages and tools.
- Move product explanation and proof higher for apps.
- Replace abstract feature lists with concrete benefits.
- Collapse duplicated sections.
- Convert long prose into clearer headings and shorter lists.
- Remove unsupported claims and stale setup steps.
- Add selective `[//]: # (...)` comments above sections that materially need a hero image, video, screenshot, or diagram.

## Smells to remove

- “Modern, scalable, robust” with no evidence
- architecture before purpose
- setup instructions that do not match project files
- screenshots or demo links mentioned but not actually present

## Final pass

Before finishing, confirm that:

- the first screenful explains the project clearly
- the reader can find the first-run path quickly
- technical depth appears after basic orientation
- every section earns its place
- any hidden improvement comments use the exact `[//]: # (...)` syntax and point to concrete upgrades
- header composition follows `header.md` rather than ad hoc top-of-file rules
