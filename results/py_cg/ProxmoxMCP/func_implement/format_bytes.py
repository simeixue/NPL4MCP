# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/formatting/formatters.py
# module: src.proxmox_mcp.formatting.formatters
# qname: src.proxmox_mcp.formatting.formatters.ProxmoxFormatters.format_bytes
# lines: 12-25
    def format_bytes(bytes_value: int) -> str:
        """Format bytes with proper units.
        
        Args:
            bytes_value: Number of bytes
            
        Returns:
            Formatted string with appropriate unit
        """
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_value < 1024:
                return f"{bytes_value:.2f} {unit}"
            bytes_value /= 1024
        return f"{bytes_value:.2f} TB"