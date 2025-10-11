# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/server.py
# module: src.semgrep_mcp.server
# qname: src.semgrep_mcp.server.get_semgrep_rule_yaml
# lines: 422-432
async def get_semgrep_rule_yaml(rule_id: str = RULE_ID_FIELD) -> str:
    """Full Semgrep rule in YAML format from the Semgrep registry."""

    try:
        response = await http_client.get(f"https://semgrep.dev/c/r/{rule_id}")
        response.raise_for_status()
        return str(response.text)
    except Exception as e:
        raise McpError(
            ErrorData(code=INTERNAL_ERROR, message=f"Error loading Semgrep rule schema: {e!s}")
        ) from e