# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/scripts/configure_semgrep_mcp.py
# module: scripts.configure_semgrep_mcp
# qname: scripts.configure_semgrep_mcp._create_safe_cmd_display
# lines: 59-72
def _create_safe_cmd_display(claude_cmd: list[str]) -> list[str]:
    """Create safe command display that masks sensitive values."""
    safe_cmd = []
    skip_next = False
    for arg in claude_cmd:
        if skip_next:
            safe_cmd.append("***")
            skip_next = False
        elif arg == "-e":
            safe_cmd.append(arg)
            skip_next = True
        else:
            safe_cmd.append(arg)
    return safe_cmd