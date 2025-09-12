# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/MiniMax-MCP/minimax_mcp/utils.py
# module: minimax_mcp.utils
# qname: minimax_mcp.utils.check_audio_file
# lines: 102-115
def check_audio_file(path: Path) -> bool:
    audio_extensions = {
        ".wav",
        ".mp3",
        ".m4a",
        ".aac",
        ".ogg",
        ".flac",
        ".mp4",
        ".avi",
        ".mov",
        ".wmv",
    }
    return path.suffix.lower() in audio_extensions