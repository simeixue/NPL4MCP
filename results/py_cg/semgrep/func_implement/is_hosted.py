# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/utilities/utils.py
# module: src.semgrep_mcp.utilities.utils
# qname: src.semgrep_mcp.utilities.utils.is_hosted
# lines: 17-21
def is_hosted() -> bool:
    """
    Check if the user is using the hosted version of the MCP server.
    """
    return os.environ.get("SEMGREP_IS_HOSTED", "false").lower() == "true"