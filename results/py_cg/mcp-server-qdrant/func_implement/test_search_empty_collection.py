# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/tests/test_qdrant_integration.py
# module: tests.test_qdrant_integration
# qname: tests.test_qdrant_integration.test_search_empty_collection
# lines: 52-58
async def test_search_empty_collection(qdrant_connector):
    """Test searching in an empty collection."""
    # Search in an empty collection
    results = await qdrant_connector.search("test query")

    # Verify results
    assert len(results) == 0