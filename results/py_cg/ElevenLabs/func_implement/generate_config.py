# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/elevenlabs/elevenlabs_mcp/__main__.py
# module: elevenlabs_mcp.__main__
# qname: elevenlabs_mcp.__main__.generate_config
# lines: 33-59
def generate_config(api_key: str | None = None):
    module_dir = Path(__file__).resolve().parent
    server_path = module_dir / "server.py"
    python_path = get_python_path()

    final_api_key = api_key or os.environ.get("ELEVENLABS_API_KEY")
    if not final_api_key:
        print("Error: ElevenLabs API key is required.")
        print("Please either:")
        print("  1. Pass the API key using --api-key argument, or")
        print("  2. Set the ELEVENLABS_API_KEY environment variable, or")
        print("  3. Add ELEVENLABS_API_KEY to your .env file")
        sys.exit(1)

    config = {
        "mcpServers": {
            "ElevenLabs": {
                "command": python_path,
                "args": [
                    str(server_path),
                ],
                "env": {"ELEVENLABS_API_KEY": final_api_key},
            }
        }
    }

    return config