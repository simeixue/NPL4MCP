# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/square-mcp/src/square_mcp/server.py
# module: src.square_mcp.server
# qname: src.square_mcp.server.team
# lines: 424-491
async def team(
    operation: str,
    params: Dict[str, Any]
) -> Dict[str, Any]:
    """Manage team operations

    Args:
        operation: The operation to perform. Valid operations:
            Team Members:
                - create_team_member
                - bulk_create_team_members
                - update_team_member
                - retrieve_team_member
                - search_team_members
            Wages:
                - retrieve_wage_setting
                - update_wage_setting
            Labor:
                - create_break_type
                - create_shift
                - search_shifts
                - update_shift
                - create_workweek_config
            Cash Drawers:
                - list_cash_drawer_shifts
                - retrieve_cash_drawer_shift
        params: Dictionary of parameters for the specific operation
    """
    try:
        match operation:
            # Team Members
            case "create_team_member":
                result = square_client.team.create_team_member(params)
            case "bulk_create_team_members":
                result = square_client.team.bulk_create_team_members(params)
            case "update_team_member":
                result = square_client.team.update_team_member(**params)
            case "retrieve_team_member":
                result = square_client.team.retrieve_team_member(**params)
            case "search_team_members":
                result = square_client.team.search_team_members(params)
            # Wages
            case "retrieve_wage_setting":
                result = square_client.labor.retrieve_wage_setting(**params)
            case "update_wage_setting":
                result = square_client.labor.update_wage_setting(**params)
            # Labor
            case "create_break_type":
                result = square_client.labor.create_break_type(params)
            case "create_shift":
                result = square_client.labor.create_shift(params)
            case "search_shifts":
                result = square_client.labor.search_shifts(params)
            case "update_shift":
                result = square_client.labor.update_shift(**params)
            case "create_workweek_config":
                result = square_client.labor.create_workweek_config(params)
            # Cash Drawers
            case "list_cash_drawer_shifts":
                result = square_client.cash_drawers.list_cash_drawer_shifts(**params)
            case "retrieve_cash_drawer_shift":
                result = square_client.cash_drawers.retrieve_cash_drawer_shift(**params)
            case _:
                raise McpError(INVALID_PARAMS, ErrorData(message=f"Invalid operation: {operation}"))

        return result.body
    except Exception as e:
        raise McpError(INTERNAL_ERROR, ErrorData(message=str(e)))