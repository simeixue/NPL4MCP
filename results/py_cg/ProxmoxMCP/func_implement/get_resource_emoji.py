# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/formatting/theme.py
# module: src.proxmox_mcp.formatting.theme
# qname: src.proxmox_mcp.formatting.theme.ProxmoxTheme.get_resource_emoji
# lines: 87-90
    def get_resource_emoji(cls, resource: str) -> str:
        """Get emoji for a resource type with fallback."""
        resource = resource.lower()
        return cls.RESOURCES.get(resource, '📦')