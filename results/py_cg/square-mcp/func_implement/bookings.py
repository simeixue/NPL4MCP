# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/square-mcp/src/square_mcp/server.py
# module: src.square_mcp.server
# qname: src.square_mcp.server.bookings
# lines: 626-684
async def bookings(
    operation: str,
    params: Dict[str, Any]
) -> Dict[str, Any]:
    """Manage booking operations

    Args:
        operation: The operation to perform. Valid operations:
            Bookings:
                - create_booking
                - search_bookings
                - retrieve_booking
                - update_booking
                - cancel_booking
            Team Member Bookings:
                - bulk_retrieve_team_member_bookings
                - retrieve_team_member_booking_profile
            Location Profiles:
                - list_location_booking_profiles
                - retrieve_location_booking_profile
            Custom Attributes:
                - create_booking_custom_attribute_definition
                - update_booking_custom_attribute_definition
        params: Dictionary of parameters for the specific operation
    """
    try:
        match operation:
            # Bookings
            case "create_booking":
                result = square_client.bookings.create_booking(params)
            case "search_bookings":
                result = square_client.bookings.search_bookings(params)
            case "retrieve_booking":
                result = square_client.bookings.retrieve_booking(**params)
            case "update_booking":
                result = square_client.bookings.update_booking(**params)
            case "cancel_booking":
                result = square_client.bookings.cancel_booking(**params)
            # Team Member Bookings
            case "bulk_retrieve_team_member_bookings":
                result = square_client.bookings.bulk_retrieve_team_member_bookings(params)
            case "retrieve_team_member_booking_profile":
                result = square_client.bookings.retrieve_team_member_booking_profile(**params)
            # Location Profiles
            case "list_location_booking_profiles":
                result = square_client.bookings.list_location_booking_profiles(**params)
            case "retrieve_location_booking_profile":
                result = square_client.bookings.retrieve_location_booking_profile(**params)
            # Custom Attributes
            case "create_booking_custom_attribute_definition":
                result = square_client.booking_custom_attributes.create_booking_custom_attribute_definition(params)
            case "update_booking_custom_attribute_definition":
                result = square_client.booking_custom_attributes.update_booking_custom_attribute_definition(**params)
            case _:
                raise McpError(INVALID_PARAMS, ErrorData(message=f"Invalid operation: {operation}"))

        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))