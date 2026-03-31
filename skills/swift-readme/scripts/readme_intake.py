#!/usr/bin/env python3

"""Generate a compact README intake brief for ambiguous repositories."""

from __future__ import annotations

import argparse
import sys


REPO_TYPES = {
    "1": ("app", "User-facing app or product"),
    "2": ("package-library", "Reusable package, library, framework, plugin, or SDK"),
    "3": ("cli-tool", "CLI, automation, generator, script collection, or internal utility"),
    "4": ("template", "Starter repo, boilerplate, or scaffold"),
    "5": ("docs-site", "Documentation-first or content-first repo"),
    "6": ("agent-skill", "Installable skill, agent playbook, or AI workflow bundle"),
    "7": ("mixed-other", "Mixed repo or something else"),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a Markdown README intake brief."
    )
    parser.add_argument(
        "--template",
        action="store_true",
        help="Compatibility alias for the template command.",
    )
    parser.add_argument(
        "--title",
        default="README Intake Brief",
        help="Heading to use at the top of the generated brief.",
    )
    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser(
        "create",
        help="Run an intake flow for creating a new README or replacing a weak one.",
    )
    subparsers.add_parser(
        "update",
        help="Run an intake flow for updating or rewriting an existing README.",
    )
    subparsers.add_parser(
        "template",
        help="Print a fill-in Markdown intake brief template.",
    )
    return parser.parse_args()


def prompt(text: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    value = input(f"{text}{suffix}: ").strip()
    return value or default


def choose_repo_type() -> tuple[str, str]:
    print("Choose the repo type that best fits this project:")
    for key, (slug, label) in REPO_TYPES.items():
        print(f"  {key}. {slug} - {label}")
    while True:
        choice = input("Repo type [1-7]: ").strip()
        if choice in REPO_TYPES:
            return REPO_TYPES[choice]
        print("Enter a number from 1 to 7.")


def format_section(title: str, items: list[tuple[str, str]]) -> str:
    lines = [f"## {title}", ""]
    for label, value in items:
        normalized = value.strip() if value.strip() else "Unknown"
        lines.append(f"- {label}: {normalized}")
    lines.append("")
    return "\n".join(lines)


def common_sections(
    repo_type: str,
    repo_type_label: str,
    audience: str,
    secondary_audience: str,
    purpose: str,
    first_screenful: str,
    first_action: str,
    main_path: str,
    platforms: str,
    toolchain: str,
    contact: str,
    license_name: str,
    missing_asset: str,
    hidden_comment: str,
    tone: str,
    must_have_sections: str,
    avoid_sections: str,
    notes: list[tuple[str, str]],
) -> list[str]:
    return [
        format_section(
            "Repo Type",
            [
                ("Type", repo_type),
                ("Confidence", "User-provided"),
                ("Description", repo_type_label),
            ],
        ),
        format_section(
            "Audience",
            [("Primary reader", audience), ("Secondary reader", secondary_audience)],
        ),
        format_section(
            "Purpose",
            [
                ("Why this repo exists", purpose),
                ("Immediate message", first_screenful),
            ],
        ),
        format_section(
            "Primary User Journey",
            [("First reader action", first_action), ("Main setup or usage path", main_path)],
        ),
        format_section(
            "Verified Metadata",
            [
                ("Supported platforms or runtimes", platforms),
                ("Language or toolchain version", toolchain),
                ("Contact or support link", contact),
                ("License", license_name),
            ],
        ),
        format_section(
            "Missing Assets Or Proof",
            [
                ("Most valuable missing asset", missing_asset),
                ("Needs hidden improvement comment", hidden_comment),
            ],
        ),
        format_section(
            "Constraints Or Preferences",
            [
                ("Tone", tone),
                ("Must-have sections", must_have_sections),
                ("Sections to avoid", avoid_sections),
            ],
        ),
        format_section("Notes For README", notes),
    ]


def interactive_create_brief(title: str) -> str:
    repo_type, repo_type_label = choose_repo_type()
    audience = prompt("Primary audience")
    secondary_audience = prompt("Secondary audience", "None")
    purpose = prompt("Why does this repo exist")
    first_screenful = prompt("What should the README make clear immediately")
    first_action = prompt("What should the reader do first")
    main_path = prompt("Main setup or usage path")
    platforms = prompt("Verified platforms or runtimes", "Unknown")
    toolchain = prompt("Verified language or toolchain version", "Unknown")
    contact = prompt("Verified contact or support link", "Unknown")
    license_name = prompt("Verified license", "Unknown")
    missing_asset = prompt(
        "Most valuable missing proof asset (screenshot, GIF, video, sample output, diagram, none)",
        "Unknown",
    )
    hidden_comment = prompt(
        "Should the README include a hidden improvement comment",
        "Unknown",
    )
    tone = prompt("Tone or style preference", "Unknown")
    must_have_sections = prompt("Must-have sections", "Unknown")
    avoid_sections = prompt("Sections to avoid", "Unknown")
    notes = prompt("Anything unusual the README should explain", "Unknown")

    sections = common_sections(
        repo_type,
        repo_type_label,
        audience,
        secondary_audience,
        purpose,
        first_screenful,
        first_action,
        main_path,
        platforms,
        toolchain,
        contact,
        license_name,
        missing_asset,
        hidden_comment,
        tone,
        must_have_sections,
        avoid_sections,
        [("README mode", "Create"), ("Additional notes", notes)],
    )

    return "\n".join([f"# {title}", ""] + sections).rstrip() + "\n"


def interactive_update_brief(title: str) -> str:
    repo_type, repo_type_label = choose_repo_type()
    audience = prompt("Primary audience")
    secondary_audience = prompt("Secondary audience", "None")
    purpose = prompt("Why does this repo exist")
    first_screenful = prompt("What should the updated README make clear immediately")
    first_action = prompt("What should the reader do first after reading the updated README")
    main_path = prompt("Main setup or usage path")
    platforms = prompt("Verified platforms or runtimes", "Unknown")
    toolchain = prompt("Verified language or toolchain version", "Unknown")
    contact = prompt("Verified contact or support link", "Unknown")
    license_name = prompt("Verified license", "Unknown")
    missing_asset = prompt(
        "Most valuable missing proof asset (screenshot, GIF, video, sample output, diagram, none)",
        "Unknown",
    )
    hidden_comment = prompt(
        "Should the README include a hidden improvement comment",
        "Unknown",
    )
    tone = prompt("Tone or style preference", "Unknown")
    must_have_sections = prompt("Sections that must stay", "Unknown")
    avoid_sections = prompt("Sections to remove or avoid", "Unknown")
    rewrite_problem = prompt(
        "What is wrong with the current README (structure, clarity, proof, metadata, tone, mixed)",
        "Unknown",
    )
    must_preserve = prompt("What content must be preserved from the current README", "Unknown")
    missing_now = prompt("What is missing from the current README", "Unknown")
    rewrite_goal = prompt("Is this a rewrite, cleanup, or focused improvement", "Unknown")
    notes = prompt("Anything unusual the updated README should explain", "Unknown")

    sections = common_sections(
        repo_type,
        repo_type_label,
        audience,
        secondary_audience,
        purpose,
        first_screenful,
        first_action,
        main_path,
        platforms,
        toolchain,
        contact,
        license_name,
        missing_asset,
        hidden_comment,
        tone,
        must_have_sections,
        avoid_sections,
        [
            ("README mode", "Update"),
            ("Rewrite diagnosis", rewrite_problem),
            ("Must preserve", must_preserve),
            ("Missing now", missing_now),
            ("Requested change style", rewrite_goal),
            ("Additional notes", notes),
        ],
    )

    return "\n".join([f"# {title}", ""] + sections).rstrip() + "\n"


def template_brief(title: str, mode: str) -> str:
    notes = """- README mode: Create
- Additional notes:"""
    if mode == "update":
        notes = """- README mode: Update
- Rewrite diagnosis:
- Must preserve:
- Missing now:
- Requested change style:
- Additional notes:"""

    return f"""# {title}

## Repo Type

- Type:
- Confidence:

## Audience

- Primary reader:
- Secondary reader:

## Purpose

- Why this repo exists:
- Immediate message:

## Primary User Journey

- First reader action:
- Main setup or usage path:

## Verified Metadata

- Supported platforms or runtimes:
- Language or toolchain version:
- Contact or support link:
- License:

## Missing Assets Or Proof

- Most valuable missing asset:
- Needs hidden improvement comment:

## Constraints Or Preferences

- Tone:
- Must-have sections:
- Sections to avoid:

## Notes For README

{notes}
"""


def main() -> int:
    args = parse_args()
    command = args.command or "create"
    if args.template:
        command = "template"

    if command == "template":
        sys.stdout.write(template_brief(args.title, "create"))
    elif command == "create":
        sys.stdout.write(interactive_create_brief(args.title))
    elif command == "update":
        sys.stdout.write(interactive_update_brief(args.title))
    else:
        raise SystemExit(f"Unknown command: {command}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
