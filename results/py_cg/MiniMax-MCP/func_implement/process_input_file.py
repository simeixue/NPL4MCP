# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/MiniMax-MCP/minimax_mcp/utils.py
# module: minimax_mcp.utils
# qname: minimax_mcp.utils.process_input_file
# lines: 118-140
def process_input_file(file_path: str, audio_content_check: bool = True) -> Path:
    if not os.path.isabs(file_path) and not os.environ.get(ENV_MINIMAX_MCP_BASE_PATH):
        raise MinimaxMcpError(
            "File path must be an absolute path if MINIMAX_MCP_BASE_PATH is not set"
        )
    path = Path(file_path)
    if not path.exists() and path.parent.exists():
        parent_directory = path.parent
        similar_files = try_find_similar_files(path.name, parent_directory)
        similar_files_formatted = ",".join([str(file) for file in similar_files])
        if similar_files:
            raise MinimaxMcpError(
                f"File ({path}) does not exist. Did you mean any of these files: {similar_files_formatted}?"
            )
        raise MinimaxMcpError(f"File ({path}) does not exist")
    elif not path.exists():
        raise MinimaxMcpError(f"File ({path}) does not exist")
    elif not path.is_file():
        raise MinimaxMcpError(f"File ({path}) is not a file")

    if audio_content_check and not check_audio_file(path):
        raise MinimaxMcpError(f"File ({path}) is not an audio or video file")
    return path