# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-metricool/src/mcp_metricool/tools/tools.py
# module: src.mcp_metricool.tools.tools
# qname: src.mcp_metricool.tools.tools.get_facebookads_campaigns
# lines: 347-364
async def get_facebookads_campaigns(init_date: str, end_date: str, blog_id: int) -> str | list[dict[str, Any]]:
    """
    Get the list of Facebook Ads Campaigns from your Metricool account.

    Args:
     init date: Init date of the period to get the data. The format is YYYYMMDD
     end date: End date of the period to get the data. The format is YYYYMMDD
     blog id: Blog id of the Metricool brand account.
    """

    url = f"{METRICOOL_BASE_URL}/stats/facebookads/campaigns?start={init_date}&end={end_date}&blogId={blog_id}&userId={METRICOOL_USER_ID}&integrationSource=MCP"

    response = await make_get_request(url)

    if not response:
        return ("Failed to get Facebook Ads Campaigns")

    return response