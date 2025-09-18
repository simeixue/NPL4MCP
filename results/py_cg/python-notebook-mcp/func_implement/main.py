# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/python-notebook-mcp/server.py
# module: server
# qname: server.main
# lines: 573-592
def main():
    """Start the MCP server."""
    print("Starting Notebook MCP Server...")
    print(f"Working directory: {os.getcwd()}")
    
    try:
        mcp.run()
    except AttributeError:
        # Fallback for different MCP versions
        try:
            mcp.start()
        except AttributeError:
            try:
                mcp.serve()
            except Exception as e:
                print(f"Error starting server with various methods: {str(e)}")
                sys.exit(1)
    except Exception as e:
        print(f"Error starting server: {str(e)}")
        sys.exit(1)