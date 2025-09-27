# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/api_utils.py
# module: webEvalAgent.src.api_utils
# qname: webEvalAgent.src.api_utils.validate_api_key
# lines: 6-27
async def validate_api_key(api_key: str) -> bool:
    """
    Validate the API key against the Operative backend service.
    
    Args:
        api_key: The API key to validate
        
    Returns:
        bool: True if the API key is valid, False otherwise
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                get_backend_url("api/validate-key"),
                headers={
                    "x-operative-api-key": api_key
                }
            )
            result = response.json()
            return result.get("valid", False)
    except Exception:
        return False