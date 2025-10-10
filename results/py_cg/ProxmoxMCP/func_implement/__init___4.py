# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/core/proxmox.py
# module: src.proxmox_mcp.core.proxmox
# qname: src.proxmox_mcp.core.proxmox.ProxmoxManager.__init__
# lines: 32-41
    def __init__(self, proxmox_config: ProxmoxConfig, auth_config: AuthConfig):
        """Initialize the Proxmox API manager.

        Args:
            proxmox_config: Proxmox connection configuration
            auth_config: Authentication configuration
        """
        self.logger = logging.getLogger("proxmox-mcp.proxmox")
        self.config = self._create_config(proxmox_config, auth_config)
        self.api = self._setup_api()