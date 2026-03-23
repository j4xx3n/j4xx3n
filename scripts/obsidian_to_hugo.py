#!/usr/bin/env python3
"""
Converts an Obsidian vault into Hugo content.

Vault structure:
  vault/
    category-name/
      article.md
      another-article.md

Output structure:
  content/
    category-name/
      article.md
      another-article.md

Rules:
- Folders become Hugo categories
- Files starting with _ or . are skipped
- Obsidian wiki links [[Page]] are converted to plain text or markdown links
- Obsidian image embeds ![[image.png]] are converted to Hugo shortcodes
- Front matter is added/completed if missing
"""

import os
import re
import sys
import shutil
from datetime import datetime
from pathlib import Path


VAULT_DIR = Path("vault")
CONTENT_DIR = Path("content")

# Folders in the vault to skip entirely
SKIP_FOLDERS = {".obsidian", ".trash", "templates", "Templates", "_templates"}

# File prefixes/suffixes to skip
SKIP_PREFIXES = ("_", ".")


def slugify(name: str) -> str:
    """Convert a filename to a URL-friendly slug."""
    name = name.lower()
    name = re.sub(r"[^\w\s-]", "", name)
    name = re.sub(r"[\s_]+", "-", name)
    name = name.strip("-")
    return name


def get_git_date(filepath: Path) -> str:
    """Get the file creation date from git history, fallback to mtime."""
    import subprocess
    try:
        result = subprocess.run(
            ["git", "log", "--follow", "--format=%aI", "--", str(filepath)],
            capture_output=True, text=True
        )
        dates = result.stdout.strip().splitlines()
        if dates:
            # Last entry = first commit = creation date
            return dates[-1]
    except Exception:
        pass
    mtime = filepath.stat().st_mtime
    return datetime.fromtimestamp(mtime).isoformat()


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Parse YAML front matter, return (meta dict, body string)."""
    if not content.startswith("---"):
        return {}, content

    end = content.find("\n---", 3)
    if end == -1:
        return {}, content

    frontmatter_str = content[3:end].strip()
    body = content[end + 4:].lstrip("\n")

    meta = {}
    for line in frontmatter_str.splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if value.startswith("[") and value.endswith("]"):
                # Simple list parsing
                items = [i.strip().strip('"').strip("'")
                         for i in value[1:-1].split(",") if i.strip()]
                meta[key] = items
            else:
                meta[key] = value

    return meta, body


def build_frontmatter(meta: dict) -> str:
    """Serialize a meta dict back to YAML front matter."""
    lines = ["---"]
    for key, value in meta.items():
        if isinstance(value, list):
            formatted = ", ".join(f'"{v}"' for v in value)
            lines.append(f'{key}: [{formatted}]')
        else:
            lines.append(f'{key}: "{value}"')
    lines.append("---")
    return "\n".join(lines) + "\n"


def convert_obsidian_syntax(body: str, category: str) -> str:
    """Convert Obsidian-specific markdown syntax to standard markdown."""

    # Convert image embeds: ![[image.png]] → ![image](image.png)
    body = re.sub(
        r"!\[\[([^\]|]+?)(?:\|[^\]]+?)?\]\]",
        lambda m: f"![{m.group(1)}](/images/{m.group(1)})",
        body
    )

    # Convert wiki links with aliases: [[Page|Alias]] → Alias
    body = re.sub(r"\[\[([^\]]+?)\|([^\]]+?)\]\]", r"\2", body)

    # Convert plain wiki links: [[Page]] → Page (plain text, no broken links)
    body = re.sub(r"\[\[([^\]]+?)\]\]", r"\1", body)

    # Convert Obsidian callouts: > [!NOTE] → Hugo blockquote
    body = re.sub(
        r"> \[!(\w+)\]\s*\n((?:> .*\n?)*)",
        lambda m: f"> **{m.group(1).title()}:** {m.group(2).replace('> ', '')}",
        body
    )

    return body


def process_file(vault_file: Path, category: str, category_dir: Path) -> None:
    """Process a single markdown file from the vault."""
    content = vault_file.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(content)

    # Fill in missing front matter
    stem = vault_file.stem
    if "title" not in meta:
        # Convert filename to title: my-article-name → My Article Name
        meta["title"] = stem.replace("-", " ").replace("_", " ").title()

    if "date" not in meta:
        meta["date"] = get_git_date(vault_file)

    if "categories" not in meta:
        meta["categories"] = [category.replace("-", " ").title()]

    if "draft" not in meta:
        meta["draft"] = "false"

    # Convert Obsidian syntax
    body = convert_obsidian_syntax(body, category)

    # Write output file (preserve original filename for slug consistency)
    out_file = category_dir / vault_file.name
    out_file.write_text(build_frontmatter(meta) + "\n" + body, encoding="utf-8")
    print(f"  [+] {category}/{vault_file.name}")


def sync_images(vault_dir: Path, static_images_dir: Path) -> None:
    """Copy any image files from the vault to Hugo's static/images directory."""
    image_exts = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".avif"}
    static_images_dir.mkdir(parents=True, exist_ok=True)

    for img in vault_dir.rglob("*"):
        if img.suffix.lower() in image_exts:
            dest = static_images_dir / img.name
            shutil.copy2(img, dest)
            print(f"  [img] {img.name}")


def main() -> None:
    if not VAULT_DIR.exists():
        print(f"Vault directory '{VAULT_DIR}' not found.")
        sys.exit(1)

    # Clean old generated content (keep manually-created files like archives.md)
    if CONTENT_DIR.exists():
        for item in CONTENT_DIR.iterdir():
            if item.is_dir() and item.name not in SKIP_FOLDERS:
                shutil.rmtree(item)
                print(f"Cleaned: content/{item.name}/")

    CONTENT_DIR.mkdir(parents=True, exist_ok=True)

    # Copy images
    print("\nSyncing images...")
    sync_images(VAULT_DIR, Path("static/images"))

    # Process each category folder
    print("\nProcessing vault categories...")
    processed = 0
    for category_path in sorted(VAULT_DIR.iterdir()):
        if not category_path.is_dir():
            continue
        if category_path.name in SKIP_FOLDERS:
            continue
        if category_path.name.startswith(SKIP_PREFIXES):
            continue

        category = category_path.name
        category_dir = CONTENT_DIR / category
        category_dir.mkdir(parents=True, exist_ok=True)

        # Add _index.md for the category listing page
        index_file = category_dir / "_index.md"
        index_file.write_text(
            f'---\ntitle: "{category.replace("-", " ").title()}"\n---\n'
        )

        # Process markdown files in this category
        md_files = sorted(
            f for f in category_path.iterdir()
            if f.suffix == ".md"
            and not f.name.startswith(SKIP_PREFIXES)
        )

        for md_file in md_files:
            process_file(md_file, category, category_dir)
            processed += 1

    print(f"\nDone: {processed} articles processed.")


if __name__ == "__main__":
    main()
