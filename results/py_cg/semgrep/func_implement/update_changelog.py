# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/scripts/bump_version.py
# module: scripts.bump_version
# qname: scripts.bump_version.update_changelog
# lines: 53-67
def update_changelog(file_path: Path, new_version: str) -> None:
    """Update CHANGELOG.md with new version."""
    content = file_path.read_text()
    today = datetime.now().strftime("%Y-%m-%d")
    new_entry = f"\n## [{new_version}] - {today}\n\n"

    if "# Changelog" in content:
        # Insert after the first line containing "# Changelog"
        parts = content.split("# Changelog", 1)
        content = parts[0] + "# Changelog" + new_entry + parts[1]
    else:
        # If no Changelog header exists, add it
        content = f"# Changelog\n{new_entry}\n{content}"

    file_path.write_text(content)