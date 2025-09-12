# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/square-mcp/src/square_mcp/server.py
# module: src.square_mcp.server
# qname: src.square_mcp.server.business
# lines: 687-748
async def business(
    operation: str,
    params: Dict[str, Any]
) -> Dict[str, Any]:
    """Manage business operations

    Args:
        operation: The operation to perform. Valid operations:
            Merchants:
                - list_merchants
                - retrieve_merchant
            Locations:
                - list_locations
                - create_location
                - retrieve_location
                - update_location
            Vendors:
                - bulk_create_vendors
                - bulk_retrieve_vendors
                - create_vendor
                - search_vendors
                - update_vendor
            Sites:
                - list_sites
        params: Dictionary of parameters for the specific operation
    """
    try:
        match operation:
            # Merchants
            case "list_merchants":
                result = square_client.merchants.list_merchants(**params)
            case "retrieve_merchant":
                result = square_client.merchants.retrieve_merchant(**params)
            # Locations
            case "list_locations":
                result = square_client.locations.list_locations()
            case "create_location":
                result = square_client.locations.create_location(params)
            case "retrieve_location":
                result = square_client.locations.retrieve_location(**params)
            case "update_location":
                result = square_client.locations.update_location(**params)
            # Vendors
            case "bulk_create_vendors":
                result = square_client.vendors.bulk_create_vendors(params)
            case "bulk_retrieve_vendors":
                result = square_client.vendors.bulk_retrieve_vendors(params)
            case "create_vendor":
                result = square_client.vendors.create_vendor(params)
            case "search_vendors":
                result = square_client.vendors.search_vendors(params)
            case "update_vendor":
                result = square_client.vendors.update_vendor(**params)
            # Sites
            case "list_sites":
                result = square_client.sites.list_sites(**params)
            case _:
                raise McpError(INVALID_PARAMS, ErrorData(message=f"Invalid operation: {operation}"))

        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))