# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/server.py
# module: src.fibery_mcp_server.server
# qname: src.fibery_mcp_server.server.serve.call_tool
# lines: 27-33
    async def call_tool(name: str, arguments: Dict[str, Any]) -> List[mcp.types.TextContent]:
        logger.info(f"Requested tool with uri: {name}")
        try:
            return await handle_tool_call(fibery_client, name, arguments)
        except Exception as e:
            logger.error(f"Tool error: {str(e)}")
            return [mcp.types.TextContent(type="text", text=f"Error: {str(e)}")]