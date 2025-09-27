# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/elevenlabs/elevenlabs_mcp/server.py
# module: elevenlabs_mcp.server
# qname: elevenlabs_mcp.server.create_voice_from_preview
# lines: 931-945
def create_voice_from_preview(
    generated_voice_id: str,
    voice_name: str,
    voice_description: str,
) -> TextContent:
    voice = client.text_to_voice.create_voice_from_preview(
        voice_name=voice_name,
        voice_description=voice_description,
        generated_voice_id=generated_voice_id,
    )

    return TextContent(
        type="text",
        text=f"Success. Voice created: {voice.name} with ID:{voice.voice_id}",
    )