# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/formatting/formatters.py
# module: src.proxmox_mcp.formatting.formatters
# qname: src.proxmox_mcp.formatting.formatters.ProxmoxFormatters.format_status
# lines: 67-79
    def format_status(status: str) -> str:
        """Format status with emoji and color.
        
        Args:
            status: Status string
            
        Returns:
            Formatted status string
        """
        status = status.lower()
        emoji = ProxmoxTheme.get_status_emoji(status)
        color = ProxmoxColors.status_color(status)
        return f"{emoji} {ProxmoxColors.colorize(status.upper(), color)}"