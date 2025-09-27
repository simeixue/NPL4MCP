# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/src/oxylabs_mcp/__init__.py
# module: src.oxylabs_mcp.__init__
# qname: src.oxylabs_mcp.__init__.OxylabsMCPServer._mcp_list_tools
# lines: 18-36
    async def _mcp_list_tools(self) -> list[MCPTool]:
        """List all available Oxylabs tools."""
        async with Context(fastmcp=self):
            tools = await self._list_tools()

            username, password = get_oxylabs_auth()
            if not username or not password:
                tools = [tool for tool in tools if tool.name not in SCRAPER_TOOLS]

            if not get_oxylabs_ai_studio_api_key():
                tools = [tool for tool in tools if tool.name not in AI_TOOLS]

            return [
                tool.to_mcp_tool(
                    name=tool.key,
                    include_fastmcp_meta=self.include_fastmcp_meta,
                )
                for tool in tools
            ]