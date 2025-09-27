# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/tests/test_qdrant_integration.py
# module: tests.test_qdrant_integration
# qname: tests.test_qdrant_integration.test_entry_without_metadata
# lines: 151-161
async def test_entry_without_metadata(qdrant_connector):
    """Test storing and retrieving entries without metadata."""
    # Store an entry without metadata
    await qdrant_connector.store(Entry(content="Entry without metadata"))

    # Search and verify
    results = await qdrant_connector.search("without metadata")

    assert len(results) == 1
    assert results[0].content == "Entry without metadata"
    assert results[0].metadata is None