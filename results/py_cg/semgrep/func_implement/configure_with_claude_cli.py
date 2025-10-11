# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/scripts/configure_semgrep_mcp.py
# module: scripts.configure_semgrep_mcp
# qname: scripts.configure_semgrep_mcp.configure_with_claude_cli
# lines: 184-242
def configure_with_claude_cli() -> bool:
    """Configure Semgrep MCP using Claude CLI commands."""
    print("🔧 Configuring Semgrep MCP using Claude CLI...")

    # Get the current directory (should be the semgrep-mcp project root)
    current_dir = Path(__file__).parent.parent

    # Validate path for security
    if not _validate_path(current_dir):
        print("❌ Invalid project directory path")
        return False

    # Build command for semgrep-mcp from current directory
    command = ["uv", "run", "--directory", str(current_dir), "semgrep-mcp"]

    # Prepare environment variables with validation
    env_vars = _prepare_env_vars()

    # Prepare environment arguments for Claude CLI
    env_args = []
    for key, value in env_vars.items():
        # Double-check key is safe
        if _validate_env_var_name(key):
            env_args.extend(["-e", f"{key}={value}"])

    # Build the full Claude CLI command for user scope (global)
    claude_cmd = [
        "claude",
        "mcp",
        "add",
        "--scope",
        "user",
        "semgrep-mcp",
        *env_args,
        "--",
        *command,
    ]

    # Safe command display (don't show sensitive values)
    safe_cmd = _create_safe_cmd_display(claude_cmd)
    print(f"🚀 Running: {' '.join(safe_cmd)}")

    try:
        result = subprocess.run(claude_cmd, capture_output=True, text=True, timeout=30)

        if result.returncode == 0:
            print("✅ Semgrep MCP configured successfully using Claude CLI")
            return True
        else:
            # Don't expose potentially sensitive stderr content
            print("❌ Claude CLI configuration failed")
            return False

    except subprocess.TimeoutExpired:
        print("❌ Claude CLI command timed out")
        return False
    except Exception as e:
        print(f"❌ Failed to run Claude CLI: {type(e).__name__}")
        return False