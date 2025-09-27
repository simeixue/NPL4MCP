# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/AbletonMCP/MCP_Server/server.py
# module: MCP_Server.server
# qname: MCP_Server.server.get_track_info
# lines: 273-286
def get_track_info(ctx: Context, track_index: int) -> str:
    """
    Get detailed information about a specific track in Ableton.
    
    Parameters:
    - track_index: The index of the track to get information about
    """
    try:
        ableton = get_ableton_connection()
        result = ableton.send_command("get_track_info", {"track_index": track_index})
        return json.dumps(result, indent=2)
    except Exception as e:
        logger.error(f"Error getting track info from Ableton: {str(e)}")
        return f"Error getting track info: {str(e)}"