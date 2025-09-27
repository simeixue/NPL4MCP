# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/AbletonMCP/MCP_Server/server.py
# module: MCP_Server.server
# qname: MCP_Server.server.create_midi_track
# lines: 289-302
def create_midi_track(ctx: Context, index: int = -1) -> str:
    """
    Create a new MIDI track in the Ableton session.
    
    Parameters:
    - index: The index to insert the track at (-1 = end of list)
    """
    try:
        ableton = get_ableton_connection()
        result = ableton.send_command("create_midi_track", {"index": index})
        return f"Created new MIDI track: {result.get('name', 'unknown')}"
    except Exception as e:
        logger.error(f"Error creating MIDI track: {str(e)}")
        return f"Error creating MIDI track: {str(e)}"