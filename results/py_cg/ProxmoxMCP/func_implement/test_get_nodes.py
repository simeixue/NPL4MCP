# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/tests/test_server.py
# module: tests.test_server
# qname: tests.test_server.test_get_nodes
# lines: 65-76
async def test_get_nodes(server, mock_proxmox):
    """Test get_nodes tool."""
    mock_proxmox.return_value.nodes.get.return_value = [
        {"node": "node1", "status": "online"},
        {"node": "node2", "status": "online"}
    ]
    response = await server.mcp.call_tool("get_nodes", {})
    result = json.loads(response[0].text)

    assert len(result) == 2
    assert result[0]["node"] == "node1"
    assert result[1]["node"] == "node2"