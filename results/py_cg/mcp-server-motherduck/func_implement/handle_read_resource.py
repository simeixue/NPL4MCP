# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-motherduck/src/mcp_server_motherduck/server.py
# module: src.mcp_server_motherduck.server
# qname: src.mcp_server_motherduck.server.build_application.handle_read_resource
# lines: 44-50
    async def handle_read_resource(uri: AnyUrl) -> str:
        """
        Read a specific note's content by its URI.
        The note name is extracted from the URI host component.
        """
        logger.info(f"Reading resource: {uri}")
        raise ValueError(f"Unsupported URI scheme: {uri.scheme}")