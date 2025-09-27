# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/MiniMax-MCP/minimax_mcp/utils.py
# module: minimax_mcp.utils
# qname: minimax_mcp.utils.build_output_path
# lines: 28-49
def build_output_path(
    output_directory: str | None, base_path: str | None = None, is_test: bool = False
) -> Path:
    # Set default base_path to desktop if not provided
    if base_path is None:
        base_path = str(Path.home() / "Desktop")
    
    # Handle output path based on output_directory
    if output_directory is None:
        output_path = Path(os.path.expanduser(base_path))
    elif not os.path.isabs(os.path.expanduser(output_directory)):
        output_path = Path(os.path.expanduser(base_path)) / Path(output_directory)
    else:
        output_path = Path(os.path.expanduser(output_directory))

    # Safety checks and directory creation
    if is_test:
        return output_path
    if not is_file_writeable(output_path):
        raise MinimaxMcpError(f"Directory ({output_path}) is not writeable")
    output_path.mkdir(parents=True, exist_ok=True)
    return output_path