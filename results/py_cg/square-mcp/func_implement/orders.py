# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/square-mcp/src/square_mcp/server.py
# module: src.square_mcp.server
# qname: src.square_mcp.server.orders
# lines: 180-236
async def orders(
    operation: str,
    params: Dict[str, Any]
) -> Dict[str, Any]:
    """Manage orders and checkout operations

    Args:
        operation: The operation to perform. Valid operations:
            Orders:
                - create_order
                - batch_retrieve_orders
                - calculate_order
                - clone_order
                - search_orders
                - pay_order
                - update_order
            Checkout:
                - create_checkout
                - create_payment_link
            Custom Attributes:
                - upsert_order_custom_attribute
                - list_order_custom_attribute_definitions
        params: Dictionary of parameters for the specific operation
    """
    try:
        match operation:
            # Orders
            case "create_order":
                result = square_client.orders.create_order(params)
            case "batch_retrieve_orders":
                result = square_client.orders.batch_retrieve_orders(params)
            case "calculate_order":
                result = square_client.orders.calculate_order(params)
            case "clone_order":
                result = square_client.orders.clone_order(params)
            case "search_orders":
                result = square_client.orders.search_orders(params)
            case "pay_order":
                result = square_client.orders.pay_order(params)
            case "update_order":
                result = square_client.orders.update_order(**params)
            # Checkout
            case "create_checkout":
                result = square_client.checkout.create_checkout(params)
            case "create_payment_link":
                result = square_client.checkout.create_payment_link(params)
            # Custom Attributes
            case "upsert_order_custom_attribute":
                result = square_client.orders.upsert_order_custom_attribute(**params)
            case "list_order_custom_attribute_definitions":
                result = square_client.orders.list_order_custom_attribute_definitions(**params)
            case _:
                raise McpError(INVALID_PARAMS, ErrorData(message=f"Invalid operation: {operation}"))

        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))