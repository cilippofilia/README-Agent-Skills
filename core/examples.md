# README Examples

Use these examples to keep generated top sections consistent across repo types.

## Apple app example

```md
<p align="center">
  <img src="Docs/Images/screenPrivacy_pill.svg" alt="ScreenPrivacy logo" width="60%" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/iOS-17.0+-b96229.svg" alt="iOS 17.0+" />
  <img src="https://img.shields.io/badge/macOS-14.0+-2980b9.svg" alt="macOS 14.0+" />
  <img src="https://img.shields.io/badge/Swift-6.0+-8e44ad.svg" alt="Swift 6.0+" />
  <a href="https://x.com/fcilia_dev">
    <img src="https://img.shields.io/badge/Contact-@fcilia_dev-95a5a6.svg?style=flat" alt="Contact @fcilia_dev" />
  </a>
</p>

# ScreenPrivacy

Protect private content from being captured or shown in the wrong context.
```

Use this shape for apps and products when the repo already has a polished brand asset and verified platform metadata.

## Swift package example

```md
<p align="center">
  <img src="Docs/Images/package-mark.svg" alt="Package logo" width="52%" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/iOS-17.0+-b96229.svg" alt="iOS 17.0+" />
  <img src="https://img.shields.io/badge/macOS-14.0+-2980b9.svg" alt="macOS 14.0+" />
  <img src="https://img.shields.io/badge/Swift-6.0+-8e44ad.svg" alt="Swift 6.0+" />
</p>

# MyPackage

Swift utilities for secure screen-state handling across Apple platforms.
```

Use this when `Package.swift` or project metadata explicitly defines supported platforms and toolchain expectations.

## CLI example with selective comments

````md
# ShotSync

Sync generated screenshots into the expected App Store Connect layout.

[//]: # (Usage section: this would benefit from a short terminal recording or GIF that shows the sync workflow from command invocation to generated output.)

## Usage

```bash
shotsync sync --input ./build/shots --output ./metadata/en-US
```
````

Use hidden comments sparingly. This pattern is appropriate when the README is clear, but a missing proof artifact would materially improve trust.

## Intake brief example

```md
# README Intake Brief

## Repo Type

- Type: agent-skill
- Confidence: User-provided
- Description: Installable skill, agent playbook, or AI workflow bundle

## Audience

- Primary reader: Agent users who want to install and trigger the skill correctly
- Secondary reader: Maintainers refining the skill

## Purpose

- Why this repo exists: It packages reusable README-writing guidance for agent runtimes
- Immediate message: This skill helps an agent inspect a repo and produce an accurate README without inventing claims
```

Use this style when the repo is ambiguous enough that the agent needs explicit intent before writing.

## Intake create command example

```bash
python3 skills/swift-readme/scripts/readme_intake.py create
```

Use `create` for net-new README work or when the existing README is too weak to preserve.

## Intake update command example

```bash
python3 skills/swift-readme/scripts/readme_intake.py update
```

Use `update` when the repository already has a README and the main task is diagnosis, cleanup, or rewriting.
