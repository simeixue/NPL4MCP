# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/scripts/bump_version.py
# module: scripts.bump_version
# qname: scripts.bump_version.bump_version
# lines: 24-33
def bump_version(current_version: str, bump_type: str) -> str:
    """Bump the version number based on semver rules."""
    major, minor, patch = map(int, current_version.split("."))

    if bump_type == "major":
        return f"{major + 1}.0.0"
    elif bump_type == "minor":
        return f"{major}.{minor + 1}.0"
    else:  # patch
        return f"{major}.{minor}.{patch + 1}"