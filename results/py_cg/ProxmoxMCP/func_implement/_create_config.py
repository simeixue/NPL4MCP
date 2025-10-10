# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/core/proxmox.py
# module: src.proxmox_mcp.core.proxmox
# qname: src.proxmox_mcp.core.proxmox.ProxmoxManager._create_config
# lines: 43-68
    def _create_config(self, proxmox_config: ProxmoxConfig, auth_config: AuthConfig) -> Dict[str, Any]:
        """Create a configuration dictionary for ProxmoxAPI.

        Merges connection and authentication configurations into a single
        dictionary suitable for ProxmoxAPI initialization. Handles:
        - Host and port configuration
        - SSL verification settings
        - Token-based authentication details
        - Service type specification

        Args:
            proxmox_config: Proxmox connection configuration (host, port, SSL settings)
            auth_config: Authentication configuration (user, token details)

        Returns:
            Dictionary containing merged configuration ready for API initialization
        """
        return {
            'host': proxmox_config.host,
            'port': proxmox_config.port,
            'user': auth_config.user,
            'token_name': auth_config.token_name,
            'token_value': auth_config.token_value,
            'verify_ssl': proxmox_config.verify_ssl,
            'service': proxmox_config.service
        }