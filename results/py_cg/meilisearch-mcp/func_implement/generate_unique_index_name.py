# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/tests/test_mcp_client.py
# module: tests.test_mcp_client
# qname: tests.test_mcp_client.generate_unique_index_name
# lines: 32-34
def generate_unique_index_name(prefix: str = "test") -> str:
    """Generate a unique index name for testing"""
    return f"{prefix}_{int(time.time() * 1000)}"