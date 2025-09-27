# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-motherduck/src/mcp_server_motherduck/__init__.py
# module: src.mcp_server_motherduck.__init__
# qname: src.mcp_server_motherduck.__init__.main.lifespan
# lines: 139-148
        async def lifespan(app: Starlette) -> AsyncIterator[None]:
            """Context manager for session manager."""
            async with session_manager.run():
                logger.info("MCP server started with StreamableHTTP session manager")
                try:
                    yield
                finally:
                    logger.info(
                        "🦆 MotherDuck MCP Server in \033[32mhttp-streamable\033[0m mode shutting down"
                    )