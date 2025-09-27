# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fetch/src/mcp_server_fetch/server.py
# module: src.mcp_server_fetch.server
# qname: src.mcp_server_fetch.server.get_robots_txt_url
# lines: 48-63
def get_robots_txt_url(url: str) -> str:
    """Get the robots.txt URL for a given website URL.

    Args:
        url: Website URL to get robots.txt for

    Returns:
        URL of the robots.txt file
    """
    # Parse the URL into components
    parsed = urlparse(url)

    # Reconstruct the base URL with just scheme, netloc, and /robots.txt path
    robots_url = urlunparse((parsed.scheme, parsed.netloc, "/robots.txt", "", "", ""))

    return robots_url