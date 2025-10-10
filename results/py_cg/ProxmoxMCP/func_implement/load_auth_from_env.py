# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/utils/auth.py
# module: src.proxmox_mcp.utils.auth
# qname: src.proxmox_mcp.utils.auth.load_auth_from_env
# lines: 16-49
def load_auth_from_env() -> ProxmoxAuth:
    """
    Load Proxmox authentication details from environment variables.

    Environment Variables:
        PROXMOX_USER: Username with realm (e.g., 'root@pam' or 'user@pve')
        PROXMOX_TOKEN_NAME: API token name
        PROXMOX_TOKEN_VALUE: API token value

    Returns:
        ProxmoxAuth: Authentication configuration

    Raises:
        ValueError: If required environment variables are missing
    """
    user = os.getenv("PROXMOX_USER")
    token_name = os.getenv("PROXMOX_TOKEN_NAME")
    token_value = os.getenv("PROXMOX_TOKEN_VALUE")

    if not all([user, token_name, token_value]):
        missing = []
        if not user:
            missing.append("PROXMOX_USER")
        if not token_name:
            missing.append("PROXMOX_TOKEN_NAME")
        if not token_value:
            missing.append("PROXMOX_TOKEN_VALUE")
        raise ValueError(f"Missing required environment variables: {', '.join(missing)}")

    return ProxmoxAuth(
        user=user,
        token_name=token_name,
        token_value=token_value,
    )