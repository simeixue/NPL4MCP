# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/scripts/configure_semgrep_mcp.py
# module: scripts.configure_semgrep_mcp
# qname: scripts.configure_semgrep_mcp.main
# lines: 350-384
def main():
    """Main configuration function."""
    print("🔧 Configuring Claude Code integration for Semgrep MCP...")
    print("🌐 Setting up global configuration for all Claude Code sessions...")

    # Check prerequisites and configure
    if not check_claude_cli_available():
        print("⚠️  Claude CLI not found. Falling back to JSON file configuration.")
        print("   For full functionality, install Claude CLI from: https://claude.ai/code")
        success = configure_with_json_file()
    else:
        print("✅ Claude CLI found. Using recommended CLI configuration method.")
        success = configure_with_claude_cli()

        # If CLI method fails, try JSON fallback
        if not success:
            print("⚠️  CLI method failed. Trying JSON file fallback...")
            success = configure_with_json_file()

    if not success:
        print("❌ Configuration failed")
        sys.exit(1)

    # Verify configuration
    verification_success = verify_configuration()

    # Print summary and next steps
    _print_configuration_summary()
    _print_next_steps(verification_success)

    print("\n✨ Semgrep MCP global configuration complete!")
    if verification_success:
        print("🌟 The MCP server is configured and ready for all Claude Code sessions!")
    else:
        print("🔧 Please verify the configuration before using.")