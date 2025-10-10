# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/tests/test_server.py
# module: tests.test_server
# qname: tests.test_server.server
# lines: 38-40
def server(mock_env_vars, mock_proxmox):
    """Fixture to create a ProxmoxMCPServer instance."""
    return ProxmoxMCPServer()