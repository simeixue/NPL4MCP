# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/scripts/bump_version.py
# module: scripts.bump_version
# qname: scripts.bump_version.write_toml
# lines: 18-21
def write_toml(file_path: Path, data: dict) -> None:
    """Write data to a TOML file."""
    with open(file_path, "wb") as f:
        tomli_w.dump(data, f)