# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/formatting/theme.py
# module: src.proxmox_mcp.formatting.theme
# qname: src.proxmox_mcp.formatting.theme.ProxmoxTheme.get_action_emoji
# lines: 93-96
    def get_action_emoji(cls, action: str) -> str:
        """Get emoji for an action with fallback."""
        action = action.lower()
        return cls.ACTIONS.get(action, cls.ACTIONS['info'])