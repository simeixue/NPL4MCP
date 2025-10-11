# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/scripts/configure_semgrep_mcp.py
# module: scripts.configure_semgrep_mcp
# qname: scripts.configure_semgrep_mcp.verify_configuration
# lines: 297-347
def verify_configuration() -> bool:
    """Verify the configuration was successful."""
    print("🔍 Verifying configuration...")

    # Check if Claude CLI can list the server
    if check_claude_cli_available():
        try:
            result = subprocess.run(
                ["claude", "mcp", "list"], capture_output=True, text=True, timeout=15
            )
            if result.returncode == 0 and "semgrep-mcp" in result.stdout:
                print("✅ Semgrep MCP found in Claude MCP server list")
                return True
            else:
                print("⚠️  Semgrep MCP not found in Claude MCP server list")
                return False
        except subprocess.TimeoutExpired:
            print("⚠️  Claude CLI verification timed out")
            return False
        except Exception:
            print("⚠️  Could not verify via Claude CLI")

    # Fallback: check if config file exists
    claude_config = Path.home() / ".claude.json"
    if claude_config.exists() and _validate_path(claude_config):
        try:
            # Check file size before loading
            if claude_config.stat().st_size > 1024 * 1024:
                print("❌ Config file too large to verify")
                return False

            with claude_config.open() as f:
                config = json.load(f)

            if (
                isinstance(config, dict)
                and "mcpServers" in config
                and isinstance(config["mcpServers"], dict)
                and "semgrep-mcp" in config["mcpServers"]
            ):
                print("✅ Semgrep MCP found in configuration file")
                return True
            else:
                print("⚠️  Semgrep MCP not found in configuration file")
                return False
        except (OSError, json.JSONDecodeError):
            print("⚠️  Could not verify configuration file")
            return False

    print("⚠️  No configuration found")
    return False