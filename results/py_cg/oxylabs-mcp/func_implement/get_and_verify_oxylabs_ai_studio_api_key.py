# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/src/oxylabs_mcp/utils.py
# module: src.oxylabs_mcp.utils
# qname: src.oxylabs_mcp.utils.get_and_verify_oxylabs_ai_studio_api_key
# lines: 231-242
def get_and_verify_oxylabs_ai_studio_api_key() -> str:
    """Extract and varify the Oxylabs AI Studio API key."""
    ai_studio_api_key = get_oxylabs_ai_studio_api_key()

    if ai_studio_api_key is None:
        msg = "AI Studio API key is not set"
        logger.warning(msg)
        raise ValueError(msg)
    if not is_api_key_valid(ai_studio_api_key):
        raise ValueError("AI Studio API key is not valid")

    return ai_studio_api_key