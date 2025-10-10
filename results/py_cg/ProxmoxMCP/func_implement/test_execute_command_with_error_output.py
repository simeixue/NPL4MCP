# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/tests/test_vm_console.py
# module: tests.test_vm_console
# qname: tests.test_vm_console.test_execute_command_with_error_output
# lines: 75-88
async def test_execute_command_with_error_output(vm_console, mock_proxmox):
    """Test command execution with error output."""
    mock_proxmox.nodes.return_value.qemu.return_value.agent.exec.post.return_value = {
        "out": "",
        "err": "command error",
        "exitcode": 1
    }

    result = await vm_console.execute_command("node1", "100", "invalid-command")

    assert result["success"] is True  # Success refers to API call, not command
    assert result["output"] == ""
    assert result["error"] == "command error"
    assert result["exit_code"] == 1