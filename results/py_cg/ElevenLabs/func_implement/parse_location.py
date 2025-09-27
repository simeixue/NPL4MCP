# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/elevenlabs/elevenlabs_mcp/utils.py
# module: elevenlabs_mcp.utils
# qname: elevenlabs_mcp.utils.parse_location
# lines: 216-236
def parse_location(api_residency: str | None) -> str:
    """
    Parse the API residency and return the corresponding origin URL.
    """
    origin_map = {
        "us": "https://api.elevenlabs.io",
        "eu-residency": "https://api.eu.residency.elevenlabs.io",
        "in-residency": "https://api.in.residency.elevenlabs.io",
        "global": "https://api.elevenlabs.io",
    }

    if not api_residency or not api_residency.strip():
        return origin_map["us"]

    api_residency = api_residency.strip().lower()

    if api_residency not in origin_map:
        valid_options = ", ".join(f"'{k}'" for k in origin_map.keys())
        raise ValueError(f"ELEVENLABS_API_RESIDENCY must be one of {valid_options}")

    return origin_map[api_residency]