# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/formatting/colors.py
# module: src.proxmox_mcp.formatting.colors
# qname: src.proxmox_mcp.formatting.colors.ProxmoxColors.status_color
# lines: 63-79
    def status_color(cls, status: str) -> str:
        """Get appropriate color for a status value.
        
        Args:
            status: Status string to get color for
            
        Returns:
            ANSI color code
        """
        status = status.lower()
        if status in ['online', 'running', 'success']:
            return cls.GREEN
        elif status in ['offline', 'stopped', 'error']:
            return cls.RED
        elif status in ['pending', 'warning']:
            return cls.YELLOW
        return cls.BLUE