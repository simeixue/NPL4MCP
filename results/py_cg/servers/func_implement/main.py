# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/servers/src/time/src/mcp_server_time/__init__.py
# module: src.time.src.mcp_server_time.__init__
# qname: src.time.src.mcp_server_time.__init__.main
# lines: 4-15
def main():
    """MCP Time Server - Time and timezone conversion functionality for MCP"""
    import argparse
    import asyncio

    parser = argparse.ArgumentParser(
        description="give a model the ability to handle time queries and timezone conversions"
    )
    parser.add_argument("--local-timezone", type=str, help="Override local timezone")

    args = parser.parse_args()
    asyncio.run(serve(args.local_timezone))