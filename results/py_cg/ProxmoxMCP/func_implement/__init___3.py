# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/tools/console/manager.py
# module: src.proxmox_mcp.tools.console.manager
# qname: src.proxmox_mcp.tools.console.manager.VMConsoleManager.__init__
# lines: 36-43
    def __init__(self, proxmox_api):
        """Initialize the VM console manager.

        Args:
            proxmox_api: Initialized ProxmoxAPI instance
        """
        self.proxmox = proxmox_api
        self.logger = logging.getLogger("proxmox-mcp.vm-console")