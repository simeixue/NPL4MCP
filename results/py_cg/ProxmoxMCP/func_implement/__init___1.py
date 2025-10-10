# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/tools/vm.py
# module: src.proxmox_mcp.tools.vm
# qname: src.proxmox_mcp.tools.vm.VMTools.__init__
# lines: 36-43
    def __init__(self, proxmox_api):
        """Initialize VM tools.

        Args:
            proxmox_api: Initialized ProxmoxAPI instance
        """
        super().__init__(proxmox_api)
        self.console_manager = VMConsoleManager(proxmox_api)