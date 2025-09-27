# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/kagimcp/src/kagimcp/server.py
# module: src.kagimcp.server
# qname: src.kagimcp.server.kagi_search_fetch
# lines: 16-32
def kagi_search_fetch(
    queries: list[str] = Field(
        description="One or more concise, keyword-focused search queries. Include essential context within each query for standalone use."
    ),
) -> str:
    """Fetch web results based on one or more queries using the Kagi Search API. Use for general search and when the user explicitly tells you to 'fetch' results/information. Results are from all queries given. They are numbered continuously, so that a user may be able to refer to a result by a specific number."""
    try:
        if not queries:
            raise ValueError("Search called with no queries.")

        with ThreadPoolExecutor() as executor:
            results = list(executor.map(kagi_client.search, queries, timeout=10))

        return format_search_results(queries, results)

    except Exception as e:
        return f"Error: {str(e) or repr(e)}"