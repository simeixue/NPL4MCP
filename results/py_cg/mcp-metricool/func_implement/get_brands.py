# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-metricool/src/mcp_metricool/tools/tools.py
# module: src.mcp_metricool.tools.tools
# qname: src.mcp_metricool.tools.tools.get_brands
# lines: 21-42
async def get_brands() -> list[dict[str, Any]]:
    """
    Get the list of brands from your Metricool account.
    """

    url = f"{METRICOOL_BASE_URL}/v2/settings/brands?userId={METRICOOL_USER_ID}&integrationSource=MCP"

    response = await make_get_request(url)
    if not response:
        return ("Failed to get brands")
    result = []
    dicts = response["data"]
    for item in dicts:
        simplified = {
            "label": item.get("label"),
            "id": item.get("id"),
            "userId": item.get("userId"),
            "networks": item.get("networksData"),
            "timezone": item.get("timezone")
        }
        result.append(simplified)
    return result