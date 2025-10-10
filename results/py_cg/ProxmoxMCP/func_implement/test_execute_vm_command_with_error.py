# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/tests/test_server.py
# module: tests.test_server
# qname: tests.test_server.test_execute_vm_command_with_error
# lines: 201-224
async def test_execute_vm_command_with_error(server, mock_proxmox):
    """Test VM command execution with command error."""
    # Mock VM status check
    mock_proxmox.return_value.nodes.return_value.qemu.return_value.status.current.get.return_value = {
        "status": "running"
    }
    # Mock command execution with error
    mock_proxmox.return_value.nodes.return_value.qemu.return_value.agent.exec.post.return_value = {
        "out": "",
        "err": "command not found",
        "exitcode": 1
    }

    response = await server.mcp.call_tool("execute_vm_command", {
        "node": "node1",
        "vmid": "100",
        "command": "invalid-command"
    })
    result = json.loads(response[0].text)

    assert result["success"] is True  # API call succeeded
    assert result["output"] == ""
    assert result["error"] == "command not found"
    assert result["exit_code"] == 1