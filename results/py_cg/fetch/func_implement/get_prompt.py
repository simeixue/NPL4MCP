# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fetch/src/mcp_server_fetch/server.py
# module: src.mcp_server_fetch.server
# qname: src.mcp_server_fetch.server.serve.get_prompt
# lines: 258-284
    async def get_prompt(name: str, arguments: dict | None) -> GetPromptResult:
        if not arguments or "url" not in arguments:
            raise McpError(ErrorData(code=INVALID_PARAMS, message="URL is required"))

        url = arguments["url"]

        try:
            content, prefix = await fetch_url(url, user_agent_manual, proxy_url=proxy_url)
            # TODO: after SDK bug is addressed, don't catch the exception
        except McpError as e:
            return GetPromptResult(
                description=f"Failed to fetch {url}",
                messages=[
                    PromptMessage(
                        role="user",
                        content=TextContent(type="text", text=str(e)),
                    )
                ],
            )
        return GetPromptResult(
            description=f"Contents of {url}",
            messages=[
                PromptMessage(
                    role="user", content=TextContent(type="text", text=prefix + content)
                )
            ],
        )