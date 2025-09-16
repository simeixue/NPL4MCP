# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/square-mcp/src/square_mcp/__init__.py
# module: src.square_mcp.__init__
# qname: src.square_mcp.__init__.main
# lines: 4-10
def main():
    """Square MCP: Square API Model Context Protocol Server."""
    parser = argparse.ArgumentParser(
        description="Provides access to Square API functionality through MCP."
    )
    parser.parse_args()
    mcp.run()