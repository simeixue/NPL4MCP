# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils.should_log_network_request
# lines: 59-98
def should_log_network_request(request) -> bool:
    """Determine if a network request should be logged based on its type and URL.

    Args:
        request: The Playwright request object

    Returns:
        bool: True if the request should be logged, False if it should be filtered out
    """
    url = request.url
    if "/node_modules/" in url:
        return False

    # Only log XHR requests
    if request.resource_type != "xhr" and request.resource_type != "fetch":
        return False

    # Skip common static file types
    extensions_to_filter = [
        ".js",
        ".css",
        ".woff",
        ".woff2",
        ".ttf",
        ".eot",
        ".svg",
        ".png",
        ".jpg",
        ".jpeg",
        ".gif",
        ".ico",
        ".map",
    ]

    for ext in extensions_to_filter:
        if url.endswith(ext) or f"{ext}?" in url:  # Handle URLs with query params
            return False

    # By default, log all XHR requests that weren't filtered
    return True