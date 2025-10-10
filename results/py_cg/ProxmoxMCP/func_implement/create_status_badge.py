# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/formatting/components.py
# module: src.proxmox_mcp.formatting.components
# qname: src.proxmox_mcp.formatting.components.ProxmoxComponents.create_status_badge
# lines: 161-172
    def create_status_badge(status: str) -> str:
        """Create a status badge with emoji.
        
        Args:
            status: Status string
            
        Returns:
            Formatted status badge string
        """
        status = status.lower()
        emoji = ProxmoxTheme.get_status_emoji(status)
        return f"{emoji} {status.upper()}"