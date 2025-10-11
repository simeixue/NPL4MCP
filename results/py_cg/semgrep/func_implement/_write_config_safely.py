# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/scripts/configure_semgrep_mcp.py
# module: scripts.configure_semgrep_mcp
# qname: scripts.configure_semgrep_mcp._write_config_safely
# lines: 93-117
def _write_config_safely(claude_config: Path, config_data: dict) -> bool:
    """Write configuration file safely with backup/restore."""
    try:
        # Create backup if file exists
        if claude_config.exists():
            backup_path = claude_config.with_suffix(".json.backup")
            claude_config.rename(backup_path)

        with claude_config.open("w") as f:
            json.dump(config_data, f, indent=2, ensure_ascii=True)

        # Remove backup on success
        backup_path = claude_config.with_suffix(".json.backup")
        if backup_path.exists():
            backup_path.unlink()

        print(f"✅ Configuration written to: {claude_config}")
        return True
    except OSError:
        print("❌ Failed to write configuration")
        # Restore backup if it exists
        backup_path = claude_config.with_suffix(".json.backup")
        if backup_path.exists():
            backup_path.rename(claude_config)
        return False