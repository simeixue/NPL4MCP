# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/square-mcp/src/square_mcp/server.py
# module: src.square_mcp.server
# qname: src.square_mcp.server.inventory
# lines: 292-333
async def inventory(
    operation: str,
    params: Dict[str, Any]
) -> Dict[str, Any]:
    """Manage inventory operations

    Args:
        operation: The operation to perform. Valid operations:
            - batch_change_inventory
            - batch_retrieve_inventory_changes
            - batch_retrieve_inventory_counts
            - retrieve_inventory_adjustment
            - retrieve_inventory_changes
            - retrieve_inventory_count
            - retrieve_inventory_physical_count
            - retrieve_inventory_transfer
        params: Dictionary of parameters for the specific operation
    """
    try:
        match operation:
            case "batch_change_inventory":
                result = square_client.inventory.batch_change_inventory(params)
            case "batch_retrieve_inventory_changes":
                result = square_client.inventory.batch_retrieve_inventory_changes(params)
            case "batch_retrieve_inventory_counts":
                result = square_client.inventory.batch_retrieve_inventory_counts(params)
            case "retrieve_inventory_adjustment":
                result = square_client.inventory.retrieve_inventory_adjustment(**params)
            case "retrieve_inventory_changes":
                result = square_client.inventory.retrieve_inventory_changes(**params)
            case "retrieve_inventory_count":
                result = square_client.inventory.retrieve_inventory_count(**params)
            case "retrieve_inventory_physical_count":
                result = square_client.inventory.retrieve_inventory_physical_count(**params)
            case "retrieve_inventory_transfer":
                result = square_client.inventory.retrieve_inventory_transfer(**params)
            case _:
                raise McpError(INVALID_PARAMS, ErrorData(message=f"Invalid operation: {operation}"))

        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))