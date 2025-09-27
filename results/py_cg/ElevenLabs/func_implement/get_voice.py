# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/elevenlabs/elevenlabs_mcp/server.py
# module: elevenlabs_mcp.server
# qname: elevenlabs_mcp.server.get_voice
# lines: 437-445
def get_voice(voice_id: str) -> McpVoice:
    """Get details of a specific voice."""
    response = client.voices.get(voice_id=voice_id)
    return McpVoice(
        id=response.voice_id,
        name=response.name,
        category=response.category,
        fine_tuning_status=response.fine_tuning.state,
    )