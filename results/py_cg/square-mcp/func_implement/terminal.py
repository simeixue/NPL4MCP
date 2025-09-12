# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/square-mcp/src/square_mcp/server.py
# module: src.square_mcp.server
# qname: src.square_mcp.server.terminal
# lines: 121-177
async def terminal(
    operation: str,
    params: Dict[str, Any]
) -> Dict[str, Any]:
    """Manage Square Terminal operations

    Args:
        operation: The operation to perform. Valid operations:
            Checkout:
                - create_terminal_checkout
                - search_terminal_checkouts
                - get_terminal_checkout
                - cancel_terminal_checkout
            Devices:
                - create_terminal_device
                - get_terminal_device
                - search_terminal_devices
            Refunds:
                - create_terminal_refund
                - search_terminal_refunds
                - get_terminal_refund
                - cancel_terminal_refund
        params: Dictionary of parameters for the specific operation
    """
    try:
        match operation:
            # Checkout
            case "create_terminal_checkout":
                result = square_client.terminal.create_terminal_checkout(params)
            case "search_terminal_checkouts":
                result = square_client.terminal.search_terminal_checkouts(params)
            case "get_terminal_checkout":
                result = square_client.terminal.get_terminal_checkout(**params)
            case "cancel_terminal_checkout":
                result = square_client.terminal.cancel_terminal_checkout(**params)
            # Devices
            case "create_terminal_device":
                result = square_client.terminal.create_terminal_device(params)
            case "get_terminal_device":
                result = square_client.terminal.get_terminal_device(**params)
            case "search_terminal_devices":
                result = square_client.terminal.search_terminal_devices(params)
            # Refunds
            case "create_terminal_refund":
                result = square_client.terminal.create_terminal_refund(params)
            case "search_terminal_refunds":
                result = square_client.terminal.search_terminal_refunds(params)
            case "get_terminal_refund":
                result = square_client.terminal.get_terminal_refund(**params)
            case "cancel_terminal_refund":
                result = square_client.terminal.cancel_terminal_refund(**params)
            case _:
                raise McpError(INVALID_PARAMS, ErrorData(message=f"Invalid operation: {operation}"))

        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))