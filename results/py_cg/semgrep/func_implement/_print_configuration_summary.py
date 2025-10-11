# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/scripts/configure_semgrep_mcp.py
# module: scripts.configure_semgrep_mcp
# qname: scripts.configure_semgrep_mcp._print_configuration_summary
# lines: 120-163
def _print_configuration_summary() -> None:
    """Print configuration summary and environment check."""
    current_dir = Path(__file__).parent.parent
    print("\n📋 Global Configuration Summary:")
    print("   🌐 Configuration Type: Global (available to all Claude Code sessions)")
    print("   📝 Server Name: semgrep-mcp")
    # Safe path display
    if _validate_path(current_dir):
        print(f"   🚀 Command: uv run --directory {current_dir} semgrep-mcp")
    else:
        print("   🚀 Command: [path validation failed]")

    print("   🌍 Environment Variables:")
    # Safe token display
    token = os.getenv("SEMGREP_APP_TOKEN")
    if token and re.match(r"^[a-zA-Z0-9_-]+$", token):
        print(f"     SEMGREP_APP_TOKEN: {'*' * min(8, len(token))}")
    else:
        print("     SEMGREP_APP_TOKEN: (not set)")

    # Check for environment variables
    print("\n🔍 Environment Check:")

    if not token:
        print("⚠️  SEMGREP_APP_TOKEN not found in environment")
        print("   This is optional but recommended for accessing Semgrep findings")
        print("   Set it with: export SEMGREP_APP_TOKEN=your_token_here")
    elif not re.match(r"^[a-zA-Z0-9_-]+$", token):
        print("⚠️  SEMGREP_APP_TOKEN has invalid format")
    else:
        print("✅ SEMGREP_APP_TOKEN is set")

    # Check if semgrep is available
    try:
        result = subprocess.run(
            ["semgrep", "--version"], capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            print("✅ Semgrep is installed and available")
        else:
            print("⚠️  Semgrep is not working properly")
    except (FileNotFoundError, subprocess.TimeoutExpired):
        print("❌ Semgrep is not installed or not responding")
        print("   Install it with: pip install semgrep")