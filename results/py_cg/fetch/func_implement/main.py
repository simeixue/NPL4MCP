# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fetch/src/mcp_server_fetch/__init__.py
# module: src.mcp_server_fetch.__init__
# qname: src.mcp_server_fetch.__init__.main
# lines: 4-21
def main():
    """MCP Fetch Server - HTTP fetching functionality for MCP"""
    import argparse
    import asyncio

    parser = argparse.ArgumentParser(
        description="give a model the ability to make web requests"
    )
    parser.add_argument("--user-agent", type=str, help="Custom User-Agent string")
    parser.add_argument(
        "--ignore-robots-txt",
        action="store_true",
        help="Ignore robots.txt restrictions",
    )
    parser.add_argument("--proxy-url", type=str, help="Proxy URL to use for requests")

    args = parser.parse_args()
    asyncio.run(serve(args.user_agent, args.ignore_robots_txt, args.proxy_url))