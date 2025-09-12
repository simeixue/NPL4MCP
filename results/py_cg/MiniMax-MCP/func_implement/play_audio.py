# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/MiniMax-MCP/minimax_mcp/server.py
# module: minimax_mcp.server
# qname: minimax_mcp.server.play_audio
# lines: 284-291
def play_audio(input_file_path: str, is_url: bool = False) -> TextContent:
    if is_url:
        play(requests.get(input_file_path).content)
        return TextContent(type="text", text=f"Successfully played audio file: {input_file_path}")
    else:
        file_path = process_input_file(input_file_path)
        play(open(file_path, "rb").read())
        return TextContent(type="text", text=f"Successfully played audio file: {file_path}")