# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/formatting/theme.py
# module: src.proxmox_mcp.formatting.theme
# qname: src.proxmox_mcp.formatting.theme.ProxmoxTheme.get_status_emoji
# lines: 81-84
    def get_status_emoji(cls, status: str) -> str:
        """Get emoji for a status value with fallback."""
        status = status.lower()
        return cls.STATUS.get(status, cls.STATUS['unknown'])