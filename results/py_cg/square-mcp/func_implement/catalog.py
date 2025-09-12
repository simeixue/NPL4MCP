# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/square-mcp/src/square_mcp/server.py
# module: src.square_mcp.server
# qname: src.square_mcp.server.catalog
# lines: 239-289
async def catalog(
    operation: str,
    params: Dict[str, Any]
) -> Dict[str, Any]:
    """Manage catalog operations

    Args:
        operation: The operation to perform. Valid operations:
            - create_catalog_object
            - batch_delete_catalog_objects
            - batch_retrieve_catalog_objects
            - batch_upsert_catalog_objects
            - create_catalog_image
            - delete_catalog_object
            - retrieve_catalog_object
            - search_catalog_objects
            - update_catalog_object
            - update_item_modifier_lists
            - update_item_taxes
        params: Dictionary of parameters for the specific operation
    """
    try:
        match operation:
            case "create_catalog_object":
                result = square_client.catalog.create_catalog_object(params)
            case "batch_delete_catalog_objects":
                result = square_client.catalog.batch_delete_catalog_objects(params)
            case "batch_retrieve_catalog_objects":
                result = square_client.catalog.batch_retrieve_catalog_objects(params)
            case "batch_upsert_catalog_objects":
                result = square_client.catalog.batch_upsert_catalog_objects(params)
            case "create_catalog_image":
                result = square_client.catalog.create_catalog_image(params)
            case "delete_catalog_object":
                result = square_client.catalog.delete_catalog_object(**params)
            case "retrieve_catalog_object":
                result = square_client.catalog.retrieve_catalog_object(**params)
            case "search_catalog_objects":
                result = square_client.catalog.search_catalog_objects(params)
            case "update_catalog_object":
                result = square_client.catalog.update_catalog_object(**params)
            case "update_item_modifier_lists":
                result = square_client.catalog.update_item_modifier_lists(params)
            case "update_item_taxes":
                result = square_client.catalog.update_item_taxes(params)
            case _:
                raise McpError(INVALID_PARAMS, ErrorData(message=f"Invalid operation: {operation}"))

        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))