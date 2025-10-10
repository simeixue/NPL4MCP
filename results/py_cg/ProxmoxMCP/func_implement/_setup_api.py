# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/core/proxmox.py
# module: src.proxmox_mcp.core.proxmox
# qname: src.proxmox_mcp.core.proxmox.ProxmoxManager._setup_api
# lines: 70-100
    def _setup_api(self) -> ProxmoxAPI:
        """Initialize and test Proxmox API connection.

        Performs the following steps:
        1. Creates ProxmoxAPI instance with configured settings
        2. Tests connection by making a version check request
        3. Validates authentication and permissions
        4. Logs connection status and any issues

        Returns:
            Initialized and tested ProxmoxAPI instance

        Raises:
            RuntimeError: If connection fails due to:
                        - Invalid host/port
                        - Authentication failure
                        - Network connectivity issues
                        - SSL certificate validation errors
        """
        try:
            self.logger.info(f"Connecting to Proxmox host: {self.config['host']}")
            api = ProxmoxAPI(**self.config)
            
            # Test connection
            api.version.get()
            self.logger.info("Successfully connected to Proxmox API")
            
            return api
        except Exception as e:
            self.logger.error(f"Failed to connect to Proxmox: {e}")
            raise RuntimeError(f"Failed to connect to Proxmox: {e}")