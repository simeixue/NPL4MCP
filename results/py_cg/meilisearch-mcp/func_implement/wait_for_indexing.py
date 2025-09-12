# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.wait_for_indexing
# lines: 37-39
async def wait_for_indexing() -> None:
    """Wait for Meilisearch indexing to complete"""
    await asyncio.sleep(INDEXING_WAIT_TIME)