# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-metricool/src/mcp_metricool/utils/utils.py
# module: src.mcp_metricool.utils.utils
# qname: src.mcp_metricool.utils.utils.make_post_request
# lines: 147-160
async def make_post_request(url: str, data: json) -> dict[str, Any] | None:
    """Make a post request to the Metricool API with proper error handling."""
    headers = {
        "X-Mc-Auth": METRICOOL_USER_TOKEN,
        "content-type": "application/json",
        "accept": "application/json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=headers, data=data, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None