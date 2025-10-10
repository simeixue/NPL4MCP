# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/tests/test_server.py
# module: tests.test_server
# qname: tests.test_server.test_get_cluster_status
# lines: 142-152
async def test_get_cluster_status(server, mock_proxmox):
    """Test get_cluster_status tool."""
    mock_proxmox.return_value.cluster.status.get.return_value = {
        "quorate": True,
        "nodes": 2
    }

    response = await server.mcp.call_tool("get_cluster_status", {})
    result = json.loads(response[0].text)
    assert result["quorate"] is True
    assert result["nodes"] == 2