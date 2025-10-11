# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/scripts/configure_semgrep_mcp.py
# module: scripts.configure_semgrep_mcp
# qname: scripts.configure_semgrep_mcp._print_next_steps
# lines: 166-181
def _print_next_steps(verification_success: bool) -> None:
    """Print next steps based on verification result."""
    print("\n🚀 Next Steps:")
    if verification_success:
        print("1. 🎉 Configuration successful! Semgrep MCP is ready to use.")
        print("2. 🔄 Restart Claude Code to load the new configuration")
        print("3. 🌐 The Semgrep MCP tools will be available in ALL Claude Code sessions")
        print("4. 🔧 Try using the tools in any conversation:")
        print("   • semgrep_scan")
        print("   • semgrep_findings")
        print("5. 📊 Check MCP status in Claude Code with: /mcp")
    else:
        print("1. ⚠️  Configuration may not be fully working")
        print("2. 🔄 Try restarting Claude Code")
        print("3. 📋 If issues persist, run: claude mcp list")
        print("4. 🔧 Or check the configuration file manually")