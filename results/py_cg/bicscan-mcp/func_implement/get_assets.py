# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/bicscan-mcp/src/bicscan_mcp/server.py
# module: src.bicscan_mcp.server
# qname: src.bicscan_mcp.server.get_assets
# lines: 89-107
async def get_assets(address: str) -> dict:
    """Get Assets holdings by CryptoAddress

    Args:
        address: EOA, CA, ENS, CNS, KNS.
    Returns:
        Dict: where assets is a list of assets
    """

    logger.info(f"Getting assets for address: {address}")
    endpoint = "/v1/scan"
    data = {
        "query": address,
        "sync": True,
        "assets": True,
        "engines": ["ofac"],
    }

    return await post_request(endpoint, data=data)