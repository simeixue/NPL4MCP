# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-metricool/src/mcp_metricool/utils/utils.py
# module: src.mcp_metricool.utils.utils
# qname: src.mcp_metricool.utils.utils.make_get_request
# lines: 134-145
async def make_get_request(url: str) -> dict[str, Any] | None:
    """Make a get request to the Metricool API with proper error handling."""
    headers = {
        "X-Mc-Auth": METRICOOL_USER_TOKEN,
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None