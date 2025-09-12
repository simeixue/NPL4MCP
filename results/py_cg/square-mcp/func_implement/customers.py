# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/square-mcp/src/square_mcp/server.py
# module: src.square_mcp.server
# qname: src.square_mcp.server.customers
# lines: 494-567
async def customers(
    operation: str,
    params: Dict[str, Any]
) -> Dict[str, Any]:
    """Manage customer operations

    Args:
        operation: The operation to perform. Valid operations:
            Customers:
                - list_customers
                - create_customer
                - delete_customer
                - retrieve_customer
                - update_customer
                - search_customers
            Groups:
                - create_customer_group
                - delete_customer_group
                - list_customer_groups
                - retrieve_customer_group
                - update_customer_group
            Segments:
                - list_customer_segments
                - retrieve_customer_segment
            Custom Attributes:
                - create_customer_custom_attribute_definition
                - delete_customer_custom_attribute_definition
                - list_customer_custom_attribute_definitions
        params: Dictionary of parameters for the specific operation
    """
    try:
        match operation:
            # Customers
            case "list_customers":
                result = square_client.customers.list_customers(**params)
            case "create_customer":
                result = square_client.customers.create_customer(params)
            case "delete_customer":
                result = square_client.customers.delete_customer(**params)
            case "retrieve_customer":
                result = square_client.customers.retrieve_customer(**params)
            case "update_customer":
                result = square_client.customers.update_customer(**params)
            case "search_customers":
                result = square_client.customers.search_customers(params)
            # Groups
            case "create_customer_group":
                result = square_client.customer_groups.create_customer_group(params)
            case "delete_customer_group":
                result = square_client.customer_groups.delete_customer_group(**params)
            case "list_customer_groups":
                result = square_client.customer_groups.list_customer_groups(**params)
            case "retrieve_customer_group":
                result = square_client.customer_groups.retrieve_customer_group(**params)
            case "update_customer_group":
                result = square_client.customer_groups.update_customer_group(**params)
            # Segments
            case "list_customer_segments":
                result = square_client.customer_segments.list_customer_segments(**params)
            case "retrieve_customer_segment":
                result = square_client.customer_segments.retrieve_customer_segment(**params)
            # Custom Attributes
            case "create_customer_custom_attribute_definition":
                result = square_client.customer_custom_attributes.create_customer_custom_attribute_definition(params)
            case "delete_customer_custom_attribute_definition":
                result = square_client.customer_custom_attributes.delete_customer_custom_attribute_definition(**params)
            case "list_customer_custom_attribute_definitions":
                result = square_client.customer_custom_attributes.list_customer_custom_attribute_definitions(**params)
            case _:
                raise McpError(INVALID_PARAMS, ErrorData(message=f"Invalid operation: {operation}"))

        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))