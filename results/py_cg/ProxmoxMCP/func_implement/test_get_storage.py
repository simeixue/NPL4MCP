# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/tests/test_server.py
# module: tests.test_server
# qname: tests.test_server.test_get_storage
# lines: 128-139
async def test_get_storage(server, mock_proxmox):
    """Test get_storage tool."""
    mock_proxmox.return_value.storage.get.return_value = [
        {"storage": "local", "type": "dir"},
        {"storage": "ceph", "type": "rbd"}
    ]

    response = await server.mcp.call_tool("get_storage", {})
    result = json.loads(response[0].text)
    assert len(result) == 2
    assert result[0]["storage"] == "local"
    assert result[1]["storage"] == "ceph"