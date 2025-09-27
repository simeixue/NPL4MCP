# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-motherduck/src/mcp_server_motherduck/server.py
# module: src.mcp_server_motherduck.server
# qname: src.mcp_server_motherduck.server.build_application.handle_get_prompt
# lines: 69-90
    async def handle_get_prompt(
        name: str, arguments: dict[str, str] | None
    ) -> types.GetPromptResult:
        """
        Generate a prompt by combining arguments with server state.
        The prompt includes all current notes and can be customized via arguments.
        """
        logger.info(f"Getting prompt: {name}::{arguments}")
        # TODO: Check where and how this is used, and how to optimize this.
        # Check postgres and sqlite servers.
        if name != "duckdb-motherduck-initial-prompt":
            raise ValueError(f"Unknown prompt: {name}")

        return types.GetPromptResult(
            description="Initial prompt for interacting with DuckDB/MotherDuck",
            messages=[
                types.PromptMessage(
                    role="user",
                    content=types.TextContent(type="text", text=PROMPT_TEMPLATE),
                )
            ],
        )