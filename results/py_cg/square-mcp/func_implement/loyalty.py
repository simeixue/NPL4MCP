# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/square-mcp/src/square_mcp/server.py
# module: src.square_mcp.server
# qname: src.square_mcp.server.loyalty
# lines: 570-623
async def loyalty(
    operation: str,
    params: Dict[str, Any]
) -> Dict[str, Any]:
    """Manage loyalty operations

    Args:
        operation: The operation to perform. Valid operations:
            Programs:
                - create_loyalty_program
                - retrieve_loyalty_program
            Accounts:
                - create_loyalty_account
                - search_loyalty_accounts
                - retrieve_loyalty_account
                - accumulate_loyalty_points
                - adjust_loyalty_points
                - search_loyalty_events
            Promotions:
                - create_loyalty_promotion
                - cancel_loyalty_promotion
        params: Dictionary of parameters for the specific operation
    """
    try:
        match operation:
            # Programs
            case "create_loyalty_program":
                result = square_client.loyalty.create_loyalty_program(params)
            case "retrieve_loyalty_program":
                result = square_client.loyalty.retrieve_loyalty_program(**params)
            # Accounts
            case "create_loyalty_account":
                result = square_client.loyalty.create_loyalty_account(params)
            case "search_loyalty_accounts":
                result = square_client.loyalty.search_loyalty_accounts(params)
            case "retrieve_loyalty_account":
                result = square_client.loyalty.retrieve_loyalty_account(**params)
            case "accumulate_loyalty_points":
                result = square_client.loyalty.accumulate_loyalty_points(**params)
            case "adjust_loyalty_points":
                result = square_client.loyalty.adjust_loyalty_points(**params)
            case "search_loyalty_events":
                result = square_client.loyalty.search_loyalty_events(params)
            # Promotions
            case "create_loyalty_promotion":
                result = square_client.loyalty.create_loyalty_promotion(**params)
            case "cancel_loyalty_promotion":
                result = square_client.loyalty.cancel_loyalty_promotion(**params)
            case _:
                raise McpError(INVALID_PARAMS, ErrorData(message=f"Invalid operation: {operation}"))

        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))