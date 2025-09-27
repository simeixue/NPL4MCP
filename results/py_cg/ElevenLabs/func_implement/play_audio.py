# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/elevenlabs/elevenlabs_mcp/server.py
# module: elevenlabs_mcp.server
# qname: elevenlabs_mcp.server.play_audio
# lines: 1103-1106
def play_audio(input_file_path: str) -> TextContent:
    file_path = handle_input_file(input_file_path)
    play(open(file_path, "rb").read(), use_ffmpeg=False)
    return TextContent(type="text", text=f"Successfully played audio file: {file_path}")