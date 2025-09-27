# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/tests/test_qdrant_integration.py
# module: tests.test_qdrant_integration
# qname: tests.test_qdrant_integration.test_ensure_collection_exists
# lines: 96-110
async def test_ensure_collection_exists(qdrant_connector):
    """Test that the collection is created if it doesn't exist."""
    # The collection shouldn't exist yet
    assert not await qdrant_connector._client.collection_exists(
        qdrant_connector._default_collection_name
    )

    # Storing an entry should create the collection
    test_entry = Entry(content="Test content")
    await qdrant_connector.store(test_entry)

    # Now the collection should exist
    assert await qdrant_connector._client.collection_exists(
        qdrant_connector._default_collection_name
    )