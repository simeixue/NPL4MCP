# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/formatting/formatters.py
# module: src.proxmox_mcp.formatting.formatters
# qname: src.proxmox_mcp.formatting.formatters.ProxmoxFormatters.format_resource_header
# lines: 82-94
    def format_resource_header(resource_type: str, name: str) -> str:
        """Format resource header with emoji and styling.
        
        Args:
            resource_type: Type of resource
            name: Resource name
            
        Returns:
            Formatted header string
        """
        emoji = ProxmoxTheme.get_resource_emoji(resource_type)
        color = ProxmoxColors.resource_color(resource_type)
        return f"\n{emoji} {ProxmoxColors.colorize(name, color, ProxmoxColors.BOLD)}"