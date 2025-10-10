# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/tools/base.py
# module: src.proxmox_mcp.tools.base
# qname: src.proxmox_mcp.tools.base.ProxmoxTool.__init__
# lines: 32-39
    def __init__(self, proxmox_api: ProxmoxAPI):
        """Initialize the tool.

        Args:
            proxmox_api: Initialized ProxmoxAPI instance
        """
        self.proxmox = proxmox_api
        self.logger = logging.getLogger(f"proxmox-mcp.{self.__class__.__name__.lower()}")