# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/core/proxmox.py
# module: src.proxmox_mcp.core.proxmox
# qname: src.proxmox_mcp.core.proxmox.ProxmoxManager.get_api
# lines: 102-112
    def get_api(self) -> ProxmoxAPI:
        """Get the initialized Proxmox API instance.
        
        Provides access to the configured and tested ProxmoxAPI instance
        for making API calls. The instance maintains connection state and
        handles authentication automatically.

        Returns:
            ProxmoxAPI instance ready for making API calls
        """
        return self.api