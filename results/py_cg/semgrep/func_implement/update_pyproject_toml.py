# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/scripts/bump_version.py
# module: scripts.bump_version
# qname: scripts.bump_version.update_pyproject_toml
# lines: 36-40
def update_pyproject_toml(file_path: Path, new_version: str) -> None:
    """Update version in pyproject.toml."""
    data = read_toml(file_path)
    data["project"]["version"] = new_version
    write_toml(file_path, data)