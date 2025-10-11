# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/server.py
# module: src.fibery_mcp_server.server
# qname: src.fibery_mcp_server.server.serve
# lines: 16-35
async def serve(fibery_host: str, fibery_api_token: str) -> Server:
    server = Server("fibery-mcp-server")
    logging.basicConfig(level=logging.INFO, stream=sys.stderr)
    logger = logging.getLogger("fibery-mcp-server")
    fibery_client = FiberyClient(fibery_host, fibery_api_token)

    @server.list_tools()
    async def list_tools() -> List[mcp.types.Tool]:
        return handle_list_tools()

    @server.call_tool()
    async def call_tool(name: str, arguments: Dict[str, Any]) -> List[mcp.types.TextContent]:
        logger.info(f"Requested tool with uri: {name}")
        try:
            return await handle_tool_call(fibery_client, name, arguments)
        except Exception as e:
            logger.error(f"Tool error: {str(e)}")
            return [mcp.types.TextContent(type="text", text=f"Error: {str(e)}")]

    return server