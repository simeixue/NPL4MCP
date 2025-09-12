# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/server.py
# module: src.meilisearch_mcp.server
# qname: src.meilisearch_mcp.server.create_server
# lines: 28-32
def create_server(
    url: str = "http://localhost:7700", api_key: Optional[str] = None
) -> "MeilisearchMCPServer":
    """Create and return a configured MeilisearchMCPServer instance"""
    return MeilisearchMCPServer(url, api_key)