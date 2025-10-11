# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/server.py
# module: src.semgrep_mcp.server
# qname: src.semgrep_mcp.server.validate_config
# lines: 134-140
def validate_config(config: str | None = None) -> str:
    """Validates semgrep configuration parameter"""
    # Allow registry references (p/ci, p/security, etc.)
    if config is None or config.startswith("p/") or config.startswith("r/") or config == "auto":
        return config or ""
    # Otherwise, treat as path and validate
    return validate_absolute_path(config, "config")