# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.create_test_index_with_documents
# lines: 70-78
async def create_test_index_with_documents(
    server: MeilisearchMCPServer, index_name: str, documents: List[Dict[str, Any]]
) -> None:
    """Helper to create index and add documents for testing"""
    await simulate_mcp_call(server, "create-index", {"uid": index_name})
    await simulate_mcp_call(
        server, "add-documents", {"indexUid": index_name, "documents": documents}
    )
    await wait_for_indexing()