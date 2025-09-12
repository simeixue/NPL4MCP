# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/square-mcp/src/square_mcp/server.py
# module: src.square_mcp.server
# qname: src.square_mcp.server.invoices
# lines: 383-421
async def invoices(
    operation: str,
    params: Dict[str, Any]
) -> Dict[str, Any]:
    """Manage invoice operations

    Args:
        operation: The operation to perform. Valid operations:
            - create_invoice
            - search_invoices
            - get_invoice
            - update_invoice
            - cancel_invoice
            - publish_invoice
            - delete_invoice
        params: Dictionary of parameters for the specific operation
    """
    try:
        match operation:
            case "create_invoice":
                result = square_client.invoices.create_invoice(params)
            case "search_invoices":
                result = square_client.invoices.search_invoices(params)
            case "get_invoice":
                result = square_client.invoices.get_invoice(**params)
            case "update_invoice":
                result = square_client.invoices.update_invoice(**params)
            case "cancel_invoice":
                result = square_client.invoices.cancel_invoice(**params)
            case "publish_invoice":
                result = square_client.invoices.publish_invoice(**params)
            case "delete_invoice":
                result = square_client.invoices.delete_invoice(**params)
            case _:
                raise McpError(INVALID_PARAMS, ErrorData(message=f"Invalid operation: {operation}"))

        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))