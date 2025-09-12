# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/tests/test_qdrant_integration.py
# module: tests.test_qdrant_integration
# qname: tests.test_qdrant_integration.test_multiple_collections
# lines: 193-225
async def test_multiple_collections(qdrant_connector):
    """Test using multiple collections with the same connector."""
    # Define two custom collection names
    collection_a = f"collection_a_{uuid.uuid4().hex}"
    collection_b = f"collection_b_{uuid.uuid4().hex}"

    # Store entries in different collections
    entry_a = Entry(
        content="This belongs to collection A", metadata={"collection": "A"}
    )
    entry_b = Entry(
        content="This belongs to collection B", metadata={"collection": "B"}
    )
    entry_default = Entry(content="This belongs to the default collection")

    await qdrant_connector.store(entry_a, collection_name=collection_a)
    await qdrant_connector.store(entry_b, collection_name=collection_b)
    await qdrant_connector.store(entry_default)

    # Search in collection A
    results_a = await qdrant_connector.search("belongs", collection_name=collection_a)
    assert len(results_a) == 1
    assert results_a[0].content == entry_a.content

    # Search in collection B
    results_b = await qdrant_connector.search("belongs", collection_name=collection_b)
    assert len(results_b) == 1
    assert results_b[0].content == entry_b.content

    # Search in default collection
    results_default = await qdrant_connector.search("belongs")
    assert len(results_default) == 1
    assert results_default[0].content == entry_default.content