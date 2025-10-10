# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/tests/test_server.py
# module: tests.test_server
# qname: tests.test_server.test_execute_vm_command_success
# lines: 155-178
async def test_execute_vm_command_success(server, mock_proxmox):
    """Test successful VM command execution."""
    # Mock VM status check
    mock_proxmox.return_value.nodes.return_value.qemu.return_value.status.current.get.return_value = {
        "status": "running"
    }
    # Mock command execution
    mock_proxmox.return_value.nodes.return_value.qemu.return_value.agent.exec.post.return_value = {
        "out": "command output",
        "err": "",
        "exitcode": 0
    }

    response = await server.mcp.call_tool("execute_vm_command", {
        "node": "node1",
        "vmid": "100",
        "command": "ls -l"
    })
    result = json.loads(response[0].text)

    assert result["success"] is True
    assert result["output"] == "command output"
    assert result["error"] == ""
    assert result["exit_code"] == 0