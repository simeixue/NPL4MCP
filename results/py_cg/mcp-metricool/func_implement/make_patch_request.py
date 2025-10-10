# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-metricool/src/mcp_metricool/utils/utils.py
# module: src.mcp_metricool.utils.utils
# qname: src.mcp_metricool.utils.utils.make_patch_request
# lines: 177-190
async def make_patch_request(url: str, data: json) -> int | None:
    """Make a patch request to the Metricool API with proper error handling."""
    headers = {
        "X-Mc-Auth": METRICOOL_USER_TOKEN,
        "content-type": "application/json",
        "accept": "application/json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.patch(url, headers=headers, data=data, timeout=30.0)
            response.raise_for_status()
            return response.status_code
        except Exception:
            return None