# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/bicscan-mcp/src/bicscan_mcp/server.py
# module: src.bicscan_mcp.server
# qname: src.bicscan_mcp.server.get_risk_score
# lines: 68-85
async def get_risk_score(address: str) -> dict:
    """Get Risk Score for Crypto, Domain Name, ENS, CNS, KNS or even Hostname Address

    Args:
        address: EOA, CA, ENS, CNS, KNS or even HostName
    Returns:
        Dict: where summary.bicscan_score is from 0 to 100. 100 is high risk.
    """

    logger.info(f"Getting risk score for address: {address}")
    endpoint = "/v1/scan"
    data = {
        "query": address,
        "sync": True,
        "assets": False,
    }

    return await post_request(endpoint, data=data)