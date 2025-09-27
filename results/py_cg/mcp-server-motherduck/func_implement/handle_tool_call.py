# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-motherduck/src/mcp_server_motherduck/server.py
# module: src.mcp_server_motherduck.server
# qname: src.mcp_server_motherduck.server.build_application.handle_tool_call
# lines: 117-138
    async def handle_tool_call(
        name: str, arguments: dict | None
    ) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
        """
        Handle tool execution requests.
        Tools can modify server state and notify clients of changes.
        """
        logger.info(f"Calling tool: {name}::{arguments}")
        try:
            if name == "query":
                if arguments is None:
                    return [
                        types.TextContent(type="text", text="Error: No query provided")
                    ]
                tool_response = db_client.query(arguments["query"])
                return [types.TextContent(type="text", text=str(tool_response))]

            return [types.TextContent(type="text", text=f"Unsupported tool: {name}")]

        except Exception as e:
            logger.error(f"Error executing tool {name}: {e}")
            raise ValueError(f"Error executing tool {name}: {str(e)}")