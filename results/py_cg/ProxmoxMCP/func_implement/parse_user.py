# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/utils/auth.py
# module: src.proxmox_mcp.utils.auth
# qname: src.proxmox_mcp.utils.auth.parse_user
# lines: 51-70
def parse_user(user: str) -> Tuple[str, str]:
    """
    Parse a Proxmox user string into username and realm.

    Args:
        user: User string in format 'username@realm'

    Returns:
        Tuple[str, str]: (username, realm)

    Raises:
        ValueError: If user string is not in correct format
    """
    try:
        username, realm = user.split("@")
        return username, realm
    except ValueError:
        raise ValueError(
            "Invalid user format. Expected 'username@realm' (e.g., 'root@pam' or 'user@pve')"
        )