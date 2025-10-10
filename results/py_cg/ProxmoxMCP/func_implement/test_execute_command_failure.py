# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/tests/test_vm_console.py
# module: tests.test_vm_console
# qname: tests.test_vm_console.test_execute_command_failure
# lines: 66-72
async def test_execute_command_failure(vm_console, mock_proxmox):
    """Test command execution failure."""
    mock_proxmox.nodes.return_value.qemu.return_value.agent.exec.post.side_effect = \
        Exception("Command failed")

    with pytest.raises(RuntimeError, match="Failed to execute command"):
        await vm_console.execute_command("node1", "100", "ls -l")