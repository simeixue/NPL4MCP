# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/tests/test_vm_console.py
# module: tests.test_vm_console
# qname: tests.test_vm_console.mock_proxmox
# lines: 11-23
def mock_proxmox():
    """Fixture to create a mock ProxmoxAPI instance."""
    mock = Mock()
    # Setup chained mock calls
    mock.nodes.return_value.qemu.return_value.status.current.get.return_value = {
        "status": "running"
    }
    mock.nodes.return_value.qemu.return_value.agent.exec.post.return_value = {
        "out": "command output",
        "err": "",
        "exitcode": 0
    }
    return mock