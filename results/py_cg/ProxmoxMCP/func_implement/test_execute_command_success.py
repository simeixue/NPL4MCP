# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/tests/test_vm_console.py
# module: tests.test_vm_console
# qname: tests.test_vm_console.test_execute_command_success
# lines: 31-44
async def test_execute_command_success(vm_console, mock_proxmox):
    """Test successful command execution."""
    result = await vm_console.execute_command("node1", "100", "ls -l")

    assert result["success"] is True
    assert result["output"] == "command output"
    assert result["error"] == ""
    assert result["exit_code"] == 0

    # Verify correct API calls
    mock_proxmox.nodes.return_value.qemu.assert_called_with("100")
    mock_proxmox.nodes.return_value.qemu.return_value.agent.exec.post.assert_called_with(
        command="ls -l"
    )