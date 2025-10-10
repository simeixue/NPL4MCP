# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-metricool/src/mcp_metricool/tools/tools.py
# module: src.mcp_metricool.tools.tools
# qname: src.mcp_metricool.tools.tools.get_pinterest_boards
# lines: 461-476
async def get_pinterest_boards(blog_id: int) -> str | dict[str, Any]:
    """
    Get the list of Pinterest boards for a specific Metricool brand (blog_id).
    If the user doesn't provide a blog_id, ask for it.

    Args:
     blog_id: Blog id of the Metricool brand account.
    """
    url = f"{METRICOOL_BASE_URL}/v2/scheduler/boards/pinterest?blogId={blog_id}&userId={METRICOOL_USER_ID}&integrationSource=MCP"

    response = await make_get_request(url)

    if not response:
        return "Failed to get pinterest boards"

    return response