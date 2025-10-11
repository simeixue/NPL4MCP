# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/scripts/configure_semgrep_mcp.py
# module: scripts.configure_semgrep_mcp
# qname: scripts.configure_semgrep_mcp._load_existing_config
# lines: 75-90
def _load_existing_config(claude_config: Path) -> dict:
    """Load existing Claude configuration safely."""
    existing_config = {}
    if claude_config.exists():
        try:
            # Check file size to prevent loading huge files
            if claude_config.stat().st_size > 1024 * 1024:  # 1MB limit
                print("❌ Config file too large")
                return {}

            with claude_config.open() as f:
                existing_config = json.load(f)
        except (OSError, json.JSONDecodeError):
            print("⚠️  Could not load existing config, creating new one")

    return existing_config