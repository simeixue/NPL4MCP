# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/scripts/configure_semgrep_mcp.py
# module: scripts.configure_semgrep_mcp
# qname: scripts.configure_semgrep_mcp.configure_with_json_file
# lines: 245-294
def configure_with_json_file() -> bool:
    """Fallback: Configure using JSON file method."""
    print("🔧 Configuring Semgrep MCP using JSON file fallback...")

    home = Path.home()
    claude_config = home / ".claude.json"
    current_dir = Path(__file__).parent.parent

    # Validate paths
    if not _validate_path(current_dir):
        print("❌ Invalid project directory path")
        return False

    if not _validate_path(claude_config.parent):
        print("❌ Invalid config directory path")
        return False

    # Prepare configuration
    config = {
        "mcpServers": {
            "semgrep-mcp": {
                "command": "uv",
                "args": ["run", "--directory", str(current_dir), "semgrep-mcp"],
                "env": {},
            }
        }
    }

    # Add environment variables with validation
    env_vars = _prepare_env_vars()
    if env_vars:
        config["mcpServers"]["semgrep-mcp"]["env"].update(env_vars)

    # Load existing config if it exists
    existing_config = _load_existing_config(claude_config)

    # Merge configurations safely
    if not isinstance(existing_config, dict):
        existing_config = {}

    if "mcpServers" not in existing_config:
        existing_config["mcpServers"] = {}

    if not isinstance(existing_config["mcpServers"], dict):
        existing_config["mcpServers"] = {}

    existing_config["mcpServers"]["semgrep-mcp"] = config["mcpServers"]["semgrep-mcp"]

    # Write configuration with safety checks
    return _write_config_safely(claude_config, existing_config)