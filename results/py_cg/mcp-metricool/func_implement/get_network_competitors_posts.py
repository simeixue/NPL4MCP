# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-metricool/src/mcp_metricool/tools/tools.py
# module: src.mcp_metricool.tools.tools
# qname: src.mcp_metricool.tools.tools.get_network_competitors_posts
# lines: 431-458
async def get_network_competitors_posts(network: str, init_date: str, end_date: str, blog_id: int, limit: int, timezone: str) -> str | dict[str, Any]:
    """
    Get the list of posts from your competitors from your Metricool brand account.
    Add interesting conclusions for my brand about my competitors and analyze their posts.

    Args:
     init date: Init date of the period to get the data. The format is YYYY-MM-DD
     end date: End date of the period to get the data. The format is YYYY-MM-DD
     network: Network to retrieve the posts. The format is "twitter", "facebook", "instagram", "youtube", "twitch" and "bluesky". Only these are accepted.
     blog id: Blog id of the Metricool brand account.
     limit: Limit of posts of competitors. By default = 50
     timezone: Timezone of the post. The format is "Europe%2FMadrid".  Use the timezone of the user extracted from the get_brands tool.
    """
    if(network=="instagram"):
        url = f"{METRICOOL_BASE_URL}/v2/analytics/competitors/{network}/publications?from={init_date}T00%3A00%3A00&to={end_date}T23%3A59%3A59&blogId={blog_id}&userId={METRICOOL_USER_ID}&limit={limit}&timezone={timezone}&integrationSource=MCP"
        response_pub = await make_get_request(url)
        url = f"{METRICOOL_BASE_URL}/v2/analytics/competitors/{network}/publications?from={init_date}T00%3A00%3A00&to={end_date}T23%3A59%3A59&blogId={blog_id}&userId={METRICOOL_USER_ID}&limit={limit}&timezone={timezone}&integrationSource=MCP"
        response_reels = await make_get_request(url)
        response={"publications":response_pub, "reels":response_reels}
    else:
        url = f"{METRICOOL_BASE_URL}/v2/analytics/competitors/{network}/posts?from={init_date}T00%3A00%3A00&to={end_date}T23%3A59%3A59&blogId={blog_id}&userId={METRICOOL_USER_ID}&limit={limit}&timezone={timezone}&integrationSource=MCP"

        response = await make_get_request(url)

    if not response:
        return ("Failed to get competitors")

    return response