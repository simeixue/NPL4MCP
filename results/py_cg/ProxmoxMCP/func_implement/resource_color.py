# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/formatting/colors.py
# module: src.proxmox_mcp.formatting.colors
# qname: src.proxmox_mcp.formatting.colors.ProxmoxColors.resource_color
# lines: 82-98
    def resource_color(cls, resource_type: str) -> str:
        """Get appropriate color for a resource type.
        
        Args:
            resource_type: Resource type to get color for
            
        Returns:
            ANSI color code
        """
        resource_type = resource_type.lower()
        if resource_type in ['node', 'vm', 'container']:
            return cls.CYAN
        elif resource_type in ['cpu', 'memory', 'network']:
            return cls.YELLOW
        elif resource_type in ['storage', 'disk']:
            return cls.MAGENTA
        return cls.BLUE