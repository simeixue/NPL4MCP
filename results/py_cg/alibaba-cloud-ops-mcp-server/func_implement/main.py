# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/examples/openapi_mcp_quickstart/server.py
# module: examples.openapi_mcp_quickstart.server
# qname: examples.openapi_mcp_quickstart.server.main
# lines: 7-14
def main():
    mcp = FastMCP("Example MCP server")
    config = {
        'ecs': ['DescribeInstances', 'DescribeRegions'],
        'vpc': ['DescribeVpcs', 'DescribeVSwitches']
    }
    api_tools.create_api_tools(mcp, config)
    mcp.run(transport='sse')