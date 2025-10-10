# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/tests/test_server.py
# module: tests.test_server
# qname: tests.test_server.test_get_node_status
# lines: 85-95
async def test_get_node_status(server, mock_proxmox):
    """Test get_node_status tool with valid parameter."""
    mock_proxmox.return_value.nodes.return_value.status.get.return_value = {
        "status": "running",
        "uptime": 123456
    }

    response = await server.mcp.call_tool("get_node_status", {"node": "node1"})
    result = json.loads(response[0].text)
    assert result["status"] == "running"
    assert result["uptime"] == 123456