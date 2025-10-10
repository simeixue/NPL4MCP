# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-metricool/src/mcp_metricool/__init__.py
# module: src.mcp_metricool.__init__
# qname: src.mcp_metricool.__init__.main
# lines: 4-6
def main() -> None:
    "Run the Metricool MCP server"
    mcp.run(transport='stdio')