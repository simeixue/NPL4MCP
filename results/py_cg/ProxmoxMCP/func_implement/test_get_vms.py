# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/tests/test_server.py
# module: tests.test_server
# qname: tests.test_server.test_get_vms
# lines: 98-110
async def test_get_vms(server, mock_proxmox):
    """Test get_vms tool."""
    mock_proxmox.return_value.nodes.get.return_value = [{"node": "node1", "status": "online"}]
    mock_proxmox.return_value.nodes.return_value.qemu.get.return_value = [
        {"vmid": "100", "name": "vm1", "status": "running"},
        {"vmid": "101", "name": "vm2", "status": "stopped"}
    ]

    response = await server.mcp.call_tool("get_vms", {})
    result = json.loads(response[0].text)
    assert len(result) > 0
    assert result[0]["name"] == "vm1"
    assert result[1]["name"] == "vm2"