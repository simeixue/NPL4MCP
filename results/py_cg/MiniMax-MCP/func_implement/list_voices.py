# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/MiniMax-MCP/minimax_mcp/server.py
# module: minimax_mcp.server
# qname: minimax_mcp.server.list_voices
# lines: 156-181
def list_voices(
    voice_type: str = "all"
):
    try:
        response_data = api_client.post("/v1/get_voice", json={'voice_type': voice_type})
        
        system_voices = response_data.get('system_voice', []) or []
        voice_cloning_voices = response_data.get('voice_cloning', []) or []
        system_voice_list = []
        voice_cloning_voice_list = []
        
        for voice in system_voices:
            system_voice_list.append(f"Name: {voice.get('voice_name')}, ID: {voice.get('voice_id')}")
        for voice in voice_cloning_voices:
            voice_cloning_voice_list.append(f"Name: {voice.get('voice_name')}, ID: {voice.get('voice_id')}")

        return TextContent(
            type="text",
            text=f"Success. System Voices: {system_voice_list}, Voice Cloning Voices: {voice_cloning_voice_list}"
        )
        
    except MinimaxAPIError as e:
        return TextContent(
            type="text",
            text=f"Failed to list voices: {str(e)}"
        )