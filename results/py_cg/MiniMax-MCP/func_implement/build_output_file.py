# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/MiniMax-MCP/minimax_mcp/utils.py
# module: minimax_mcp.utils
# qname: minimax_mcp.utils.build_output_file
# lines: 19-25
def build_output_file(
    tool: str, text: str, output_path: Path, extension: str, full_id: bool = False
) -> Path:
    id = text if full_id else text[:10]

    output_file_name = f"{tool}_{id.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{extension}"
    return output_path / output_file_name