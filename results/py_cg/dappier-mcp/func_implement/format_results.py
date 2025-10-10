# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dappier-mcp/src/dappier_mcp/server.py
# module: src.dappier_mcp.server
# qname: src.dappier_mcp.server.format_results
# lines: 143-166
def format_results(response: AIRecommendationsResponse) -> str:
    """
    Helper function to format the API response into a human-readable string.
    """
    if response.status != "success":
        return "The API response was not successful."

    query = response.response.query or "No query provided"
    results = response.response.results or []

    formatted_text = f"Search Query: {query}\n\n"
    for idx, result in enumerate(results, start=1):
        formatted_text += (
            f"Result {idx}:\n"
            f"Title: {result.title or 'No title'}\n"
            f"Author: {result.author or 'Unknown author'}\n"
            f"Published on: {result.pubdate or 'No date available'}\n"
            f"Source: {result.site or 'Unknown site'} ({result.site_domain or 'No domain'})\n"
            f"URL: {result.source_url or 'No URL available'}\n"
            f"Image URL: {result.image_url or 'No URL available'}\n"
            f"Summary: {result.summary or 'No summary available'}\n"
            f"Score: {result.score or 'No score available'}\n\n"
        )
    return formatted_text