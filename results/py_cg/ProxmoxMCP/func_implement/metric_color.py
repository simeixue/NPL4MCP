# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/formatting/colors.py
# module: src.proxmox_mcp.formatting.colors
# qname: src.proxmox_mcp.formatting.colors.ProxmoxColors.metric_color
# lines: 101-116
    def metric_color(cls, value: float, warning: float = 80.0, critical: float = 90.0) -> str:
        """Get appropriate color for a metric value based on thresholds.
        
        Args:
            value: Metric value (typically percentage)
            warning: Warning threshold
            critical: Critical threshold
            
        Returns:
            ANSI color code
        """
        if value >= critical:
            return cls.RED
        elif value >= warning:
            return cls.YELLOW
        return cls.GREEN