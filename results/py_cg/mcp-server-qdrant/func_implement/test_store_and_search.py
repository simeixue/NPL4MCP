# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/tests/test_qdrant_integration.py
# module: tests.test_qdrant_integration
# qname: tests.test_qdrant_integration.test_store_and_search
# lines: 33-48
async def test_store_and_search(qdrant_connector):
    """Test storing an entry and then searching for it."""
    # Store a test entry
    test_entry = Entry(
        content="The quick brown fox jumps over the lazy dog",
        metadata={"source": "test", "importance": "high"},
    )
    await qdrant_connector.store(test_entry)

    # Search for the entry
    results = await qdrant_connector.search("fox jumps")

    # Verify results
    assert len(results) == 1
    assert results[0].content == test_entry.content
    assert results[0].metadata == test_entry.metadata