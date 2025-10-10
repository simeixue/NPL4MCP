# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/tests/test_server.py
# module: tests.test_server
# qname: tests.test_server.test_get_containers
# lines: 113-125
async def test_get_containers(server, mock_proxmox):
    """Test get_containers tool."""
    mock_proxmox.return_value.nodes.get.return_value = [{"node": "node1", "status": "online"}]
    mock_proxmox.return_value.nodes.return_value.lxc.get.return_value = [
        {"vmid": "200", "name": "container1", "status": "running"},
        {"vmid": "201", "name": "container2", "status": "stopped"}
    ]

    response = await server.mcp.call_tool("get_containers", {})
    result = json.loads(response[0].text)
    assert len(result) > 0
    assert result[0]["name"] == "container1"
    assert result[1]["name"] == "container2"