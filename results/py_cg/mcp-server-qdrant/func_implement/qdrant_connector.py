# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/tests/test_qdrant_integration.py
# module: tests.test_qdrant_integration
# qname: tests.test_qdrant_integration.qdrant_connector
# lines: 16-29
async def qdrant_connector(embedding_provider):
    """Fixture to provide a QdrantConnector with in-memory Qdrant client."""
    # Use a random collection name to avoid conflicts between tests
    collection_name = f"test_collection_{uuid.uuid4().hex}"

    # Create connector with in-memory Qdrant
    connector = QdrantConnector(
        qdrant_url=":memory:",
        qdrant_api_key=None,
        collection_name=collection_name,
        embedding_provider=embedding_provider,
    )

    yield connector