# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/scripts/configure_semgrep_mcp.py
# module: scripts.configure_semgrep_mcp
# qname: scripts.configure_semgrep_mcp._validate_path
# lines: 19-31
def _validate_path(path: Path) -> bool:
    """Validate path to prevent directory traversal."""
    try:
        # Resolve and check if path is within reasonable bounds
        resolved = path.resolve()
        # Must be absolute and not contain suspicious patterns
        return (
            resolved.is_absolute()
            and ".." not in path.parts
            and not any(part.startswith(".") and len(part) > 1 for part in path.parts[1:])
        )
    except (OSError, ValueError):
        return False