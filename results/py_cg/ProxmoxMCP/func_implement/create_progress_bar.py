# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/formatting/components.py
# module: src.proxmox_mcp.formatting.components
# qname: src.proxmox_mcp.formatting.components.ProxmoxComponents.create_progress_bar
# lines: 85-101
    def create_progress_bar(value: float, total: float, width: int = 20) -> str:
        """Create a progress bar with percentage.
        
        Args:
            value: Current value
            total: Maximum value
            width: Width of progress bar in characters
            
        Returns:
            Formatted progress bar string
        """
        percentage = min(100, (value / total * 100) if total > 0 else 0)
        filled = int(width * percentage / 100)
        color = ProxmoxColors.metric_color(percentage)
        
        bar = "█" * filled + "░" * (width - filled)
        return f"{ProxmoxColors.colorize(bar, color)} {percentage:.1f}%"