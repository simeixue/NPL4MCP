# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/formatting/formatters.py
# module: src.proxmox_mcp.formatting.formatters
# qname: src.proxmox_mcp.formatting.formatters.ProxmoxFormatters.format_uptime
# lines: 28-49
    def format_uptime(seconds: int) -> str:
        """Format uptime in seconds to human readable format.
        
        Args:
            seconds: Uptime in seconds
            
        Returns:
            Formatted uptime string
        """
        days = seconds // 86400
        hours = (seconds % 86400) // 3600
        minutes = (seconds % 3600) // 60
        
        parts = []
        if days > 0:
            parts.append(f"{days}d")
        if hours > 0:
            parts.append(f"{hours}h")
        if minutes > 0:
            parts.append(f"{minutes}m")
            
        return f"{ProxmoxTheme.METRICS['uptime']} " + " ".join(parts) if parts else "0m"