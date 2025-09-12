# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/config/config.py
# module: src.dbt_mcp.config.config
# qname: src.dbt_mcp.config.config._find_available_port
# lines: 173-190
def _find_available_port(*, start_port: int, max_attempts: int = 20) -> int:
    """
    Return the first available port on 127.0.0.1 starting at start_port.

    Raises RuntimeError if no port is found within the attempted range.
    """
    for candidate_port in range(start_port, start_port + max_attempts):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                sock.bind(("127.0.0.1", candidate_port))
            except OSError:
                continue
            return candidate_port
    raise RuntimeError(
        "No available port found starting at "
        f"{start_port} after {max_attempts} attempts."
    )