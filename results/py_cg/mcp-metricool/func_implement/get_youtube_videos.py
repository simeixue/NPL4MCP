# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-metricool/src/mcp_metricool/tools/tools.py
# module: src.mcp_metricool.tools.tools
# qname: src.mcp_metricool.tools.tools.get_youtube_videos
# lines: 307-324
async def get_youtube_videos(init_date: str, end_date: str, blog_id: int) -> str | dict[str, Any]:
    """
    Get the list of Youtube Videos from your Metricool brand account.

    Args:
     init date: Init date of the period to get the data. The format is YYYY-MM-DD
     end date: End date of the period to get the data. The format is YYYY-MM-DD
     blog id: Blog id of the Metricool brand account.
    """

    url = f"{METRICOOL_BASE_URL}/v2/analytics/posts/youtube?from={init_date}T00%3A00%3A00&to={end_date}T23%3A59%3A59&blogId={blog_id}&userId={METRICOOL_USER_ID}&integrationSource=MCP"

    response = await make_get_request(url)

    if not response:
        return ("Failed to get Youtube Videos")

    return response