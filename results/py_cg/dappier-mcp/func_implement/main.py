# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dappier-mcp/src/dappier_mcp/server.py
# module: src.dappier_mcp.server
# qname: src.dappier_mcp.server.main
# lines: 168-178
def main():
    """
    Entry point for the Dappier MCP server.
    
    This function initializes the FastMCP server and starts it, so that the server can begin
    processing incoming tool requests.
    """
    try:
        mcp.run()
    except Exception as e:
        print(f"Error starting MCP server: {str(e)}")