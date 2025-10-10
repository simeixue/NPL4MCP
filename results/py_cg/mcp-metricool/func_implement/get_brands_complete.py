# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-metricool/src/mcp_metricool/tools/tools.py
# module: src.mcp_metricool.tools.tools
# qname: src.mcp_metricool.tools.tools.get_brands_complete
# lines: 45-64
async def get_brands_complete() -> str | dict[str, Any]:
    """
    Get the list of brands from your Metricool account. Only use this tool if the user asks specifically for his brands, in every other case
    use get_brands.
    Add to the result that the only networks with competitors are Instagram, Facebook, Twitch, YouTube, Twitter, and Bluesky.
    """

    url = f"{METRICOOL_BASE_URL}/v2/settings/brands?userId={METRICOOL_USER_ID}&integrationSource=MCP"

    response = await make_get_request(url)

    if not response:
        return ("Failed to get brands")

    return {
    "brands": response,
    "instructions": (
        "Explain that only Instagram, Facebook, Twitch, YouTube, Twitter, and Bluesky support competitors. "
    )
}