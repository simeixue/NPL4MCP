# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/formatting/formatters.py
# module: src.proxmox_mcp.formatting.formatters
# qname: src.proxmox_mcp.formatting.formatters.ProxmoxFormatters.format_percentage
# lines: 52-64
    def format_percentage(value: float, warning: float = 80.0, critical: float = 90.0) -> str:
        """Format percentage with color based on thresholds.
        
        Args:
            value: Percentage value
            warning: Warning threshold
            critical: Critical threshold
            
        Returns:
            Formatted percentage string
        """
        color = ProxmoxColors.metric_color(value, warning, critical)
        return ProxmoxColors.colorize(f"{value:.1f}%", color)