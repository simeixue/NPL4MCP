# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/utils/auth.py
# module: src.proxmox_mcp.utils.auth
# qname: src.proxmox_mcp.utils.auth.get_auth_dict
# lines: 72-86
def get_auth_dict(auth: ProxmoxAuth) -> Dict[str, str]:
    """
    Convert ProxmoxAuth model to dictionary for Proxmoxer API.

    Args:
        auth: ProxmoxAuth configuration

    Returns:
        Dict[str, str]: Authentication dictionary for Proxmoxer
    """
    return {
        "user": auth.user,
        "token_name": auth.token_name,
        "token_value": auth.token_value,
    }