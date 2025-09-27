# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/src/oxylabs_mcp/exceptions.py
# module: src.oxylabs_mcp.exceptions
# qname: src.oxylabs_mcp.exceptions.MCPServerError.process
# lines: 7-11
    async def process(self) -> str:
        """Process exception."""
        err = str(self)
        await get_context().error(err)
        return err