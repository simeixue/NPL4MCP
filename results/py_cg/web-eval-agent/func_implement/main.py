# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/mcp_server.py
# module: webEvalAgent.mcp_server
# qname: webEvalAgent.mcp_server.main
# lines: 143-149
def main():
     try:
         # Run the FastMCP server
         mcp.run(transport='stdio')
     finally:
         # Ensure resources are cleaned up when server terminates
         pass