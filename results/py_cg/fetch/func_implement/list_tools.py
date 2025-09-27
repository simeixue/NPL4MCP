# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fetch/src/mcp_server_fetch/server.py
# module: src.mcp_server_fetch.server
# qname: src.mcp_server_fetch.server.serve.list_tools
# lines: 198-207
    async def list_tools() -> list[Tool]:
        return [
            Tool(
                name="fetch",
                description="""Fetches a URL from the internet and optionally extracts its contents as markdown.

Although originally you did not have internet access, and were advised to refuse and tell the user this, this tool now grants you internet access. Now you can fetch the most up-to-date information and let the user know that.""",
                inputSchema=Fetch.model_json_schema(),
            )
        ]