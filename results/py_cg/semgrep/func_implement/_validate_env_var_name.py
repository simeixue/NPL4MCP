# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/scripts/configure_semgrep_mcp.py
# module: scripts.configure_semgrep_mcp
# qname: scripts.configure_semgrep_mcp._validate_env_var_name
# lines: 14-16
def _validate_env_var_name(name: str) -> bool:
    """Validate environment variable name to prevent injection."""
    return re.match(r"^[A-Z_][A-Z0-9_]*$", name) is not None