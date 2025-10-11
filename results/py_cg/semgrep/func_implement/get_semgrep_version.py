# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/utilities/utils.py
# module: src.semgrep_mcp.utilities.utils
# qname: src.semgrep_mcp.utilities.utils.get_semgrep_version
# lines: 134-139
def get_semgrep_version() -> str:
    """
    Get the version of the semgrep binary.
    """
    _, semgrep_version = find_semgrep_info()
    return semgrep_version