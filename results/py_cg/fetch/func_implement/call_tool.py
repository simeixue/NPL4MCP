# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fetch/src/mcp_server_fetch/server.py
# module: src.mcp_server_fetch.server
# qname: src.mcp_server_fetch.server.serve.call_tool
# lines: 224-255
    async def call_tool(name, arguments: dict) -> list[TextContent]:
        try:
            args = Fetch(**arguments)
        except ValueError as e:
            raise McpError(ErrorData(code=INVALID_PARAMS, message=str(e)))

        url = str(args.url)
        if not url:
            raise McpError(ErrorData(code=INVALID_PARAMS, message="URL is required"))

        if not ignore_robots_txt:
            await check_may_autonomously_fetch_url(url, user_agent_autonomous, proxy_url)

        content, prefix = await fetch_url(
            url, user_agent_autonomous, force_raw=args.raw, proxy_url=proxy_url
        )
        original_length = len(content)
        if args.start_index >= original_length:
            content = "<error>No more content available.</error>"
        else:
            truncated_content = content[args.start_index : args.start_index + args.max_length]
            if not truncated_content:
                content = "<error>No more content available.</error>"
            else:
                content = truncated_content
                actual_content_length = len(truncated_content)
                remaining_content = original_length - (args.start_index + actual_content_length)
                # Only add the prompt to continue fetching if there is still remaining content
                if actual_content_length == args.max_length and remaining_content > 0:
                    next_start = args.start_index + actual_content_length
                    content += f"\n\n<error>Content truncated. Call the fetch tool with a start_index of {next_start} to get more content.</error>"
        return [TextContent(type="text", text=f"{prefix}Contents of {url}:\n{content}")]