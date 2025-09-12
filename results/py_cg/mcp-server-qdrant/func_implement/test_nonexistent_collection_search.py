# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/tests/test_qdrant_integration.py
# module: tests.test_qdrant_integration
# qname: tests.test_qdrant_integration.test_nonexistent_collection_search
# lines: 229-238
async def test_nonexistent_collection_search(qdrant_connector):
    """Test searching in a collection that doesn't exist."""
    # Search in a collection that doesn't exist
    nonexistent_collection = f"nonexistent_{uuid.uuid4().hex}"
    results = await qdrant_connector.search(
        "test query", collection_name=nonexistent_collection
    )

    # Verify results
    assert len(results) == 0