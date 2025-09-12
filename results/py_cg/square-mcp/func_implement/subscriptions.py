# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/square-mcp/src/square_mcp/server.py
# module: src.square_mcp.server
# qname: src.square_mcp.server.subscriptions
# lines: 336-380
async def subscriptions(
    operation: str,
    params: Dict[str, Any]
) -> Dict[str, Any]:
    """Manage subscription operations

    Args:
        operation: The operation to perform. Valid operations:
            - create_subscription
            - search_subscriptions
            - retrieve_subscription
            - update_subscription
            - cancel_subscription
            - list_subscription_events
            - pause_subscription
            - resume_subscription
            - swap_plan
        params: Dictionary of parameters for the specific operation
    """
    try:
        match operation:
            case "create_subscription":
                result = square_client.subscriptions.create_subscription(params)
            case "search_subscriptions":
                result = square_client.subscriptions.search_subscriptions(params)
            case "retrieve_subscription":
                result = square_client.subscriptions.retrieve_subscription(**params)
            case "update_subscription":
                result = square_client.subscriptions.update_subscription(**params)
            case "cancel_subscription":
                result = square_client.subscriptions.cancel_subscription(**params)
            case "list_subscription_events":
                result = square_client.subscriptions.list_subscription_events(**params)
            case "pause_subscription":
                result = square_client.subscriptions.pause_subscription(**params)
            case "resume_subscription":
                result = square_client.subscriptions.resume_subscription(**params)
            case "swap_plan":
                result = square_client.subscriptions.swap_plan(**params)
            case _:
                raise McpError(INVALID_PARAMS, ErrorData(message=f"Invalid operation: {operation}"))

        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))