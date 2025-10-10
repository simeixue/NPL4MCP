# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-metricool/src/mcp_metricool/tools/tools.py
# module: src.mcp_metricool.tools.tools
# qname: src.mcp_metricool.tools.tools.get_scheduled_posts
# lines: 557-577
async def get_scheduled_posts(blog_id: int, start: str, end: str, timezone: str, extendedRange: bool) -> str | dict[str, Any]:
    """
    Get the list of scheduled posts for a specific Metricool brand (blog_id).
    Only retrieves posts that are scheduled (not yet published).
    If the user doesn't provide a blog_id, ask for it.

    Args:
     blog_id: Blog id of the Metricool brand account.
     start: Start date of the period to get the data. The format is YYYY-MM-DD
     end: End date of the period to get the data. The format is YYYY-MM-DD
     timezone: Timezone of the post. The format is "Europe%2FMadrid".  Use the timezone of the user extracted from the get_brands tool.
     extendedRange: When it's true, search date range is expanded one day after and one day before. Default value is false.
    """
    url = f"{METRICOOL_BASE_URL}/v2/scheduler/posts?blogId={blog_id}&userId={METRICOOL_USER_ID}&integrationSource=MCP&start={start}T00%3A00%3A00&end={end}T23%3A59%3A59&timezone={timezone}&extendedRange={extendedRange}"

    response = await make_get_request(url)

    if not response:
        return "Failed to get scheduled posts"

    return response