# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/bicscan-mcp/src/bicscan_mcp/server.py
# module: src.bicscan_mcp.server
# qname: src.bicscan_mcp.server.post_request
# lines: 40-64
async def post_request(
    endpoint: str, data: dict[str, Any] | None = None
) -> dict[str, Any] | None:
    """Make a request to BICScan API with proper error handling."""
    headers = {
        "User-Agent": "bicscan-mcp/1.0",
        "Accept": "application/json",
        "X-Api-Key": BICSCAN_API_KEY,
    }
    url = urljoin(BICSCAN_API_BASE, endpoint)

    async with httpx.AsyncClient() as client:
        try:
            logger.info(f"Making request to {url}")
            logger.debug(f"{headers=} {data=}")
            response = await client.post(url, headers=headers, json=data, timeout=30)
            response.raise_for_status()
            logger.info(f"Received response: {response.status_code}")
            return response.json()
        except httpx.HTTPStatusError as http_err:
            logger.error(f"Received response: {http_err}, {response.text}")
            return response.json()
        except Exception as e:
            logger.exception(f"Received response: {e}, {response.text}")
            return {}