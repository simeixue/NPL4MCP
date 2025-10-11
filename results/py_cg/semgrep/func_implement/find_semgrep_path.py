# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/utilities/utils.py
# module: src.semgrep_mcp.utilities.utils
# qname: src.semgrep_mcp.utilities.utils.find_semgrep_path
# lines: 123-131
def find_semgrep_path() -> str | None:
    """
    Find the path to the semgrep executable

    Returns:
        Path to semgrep executable or None if not found
    """
    semgrep_path, _ = find_semgrep_info()
    return semgrep_path