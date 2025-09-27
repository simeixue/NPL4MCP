# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/MiniMax-MCP/minimax_mcp/__main__.py
# module: minimax_mcp.__main__
# qname: minimax_mcp.__main__.generate_config
# lines: 33-64
def generate_config(api_key: str | None = None):
    module_dir = Path(__file__).resolve().parent
    server_path = module_dir / "server.py"
    python_path = get_python_path()

    final_api_key = api_key or os.environ.get("MINIMAX_API_KEY")
    if not final_api_key:
        print("Error: Minimax API key is required.")
        print("Please either:")
        print("  1. Pass the API key using --api-key argument, or")
        print("  2. Set the MINIMAX_API_KEY environment variable, or")
        print("  3. Add MINIMAX_API_KEY to your .env file")
        sys.exit(1)

    config = {
        "mcpServers": {
            "Minimax": {
                "command": "uvx",
                "args": [
                    "minimax-mcp",
                ],

                "env": {
                    "MINIMAX_API_KEY": final_api_key,
                    "MINIMAX_MCP_BASE_PATH": "",
                    "MINIMAX_API_HOST": "https://api.minimax.chat",
                },
            }
        }
    }

    return config