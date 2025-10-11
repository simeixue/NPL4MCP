# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/scripts/bump_version.py
# module: scripts.bump_version
# qname: scripts.bump_version.read_toml
# lines: 12-15
def read_toml(file_path: Path) -> dict:
    """Read and parse a TOML file."""
    with open(file_path, "rb") as f:
        return tomli.load(f)