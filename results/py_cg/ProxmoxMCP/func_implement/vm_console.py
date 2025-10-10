# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/tests/test_vm_console.py
# module: tests.test_vm_console
# qname: tests.test_vm_console.vm_console
# lines: 26-28
def vm_console(mock_proxmox):
    """Fixture to create a VMConsoleManager instance."""
    return VMConsoleManager(mock_proxmox)