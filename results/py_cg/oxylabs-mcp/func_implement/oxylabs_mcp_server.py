# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/tests/e2e/test_llm_agent.py
# module: tests.e2e.test_llm_agent
# qname: tests.e2e.test_llm_agent.oxylabs_mcp_server
# lines: 46-61
async def oxylabs_mcp_server():
    if MCP_SERVER == "local":
        command = f"uv run --directory {os.getenv('LOCAL_OXYLABS_MCP_DIRECTORY')} oxylabs-mcp"
    elif MCP_SERVER == "uvx":
        command = "uvx oxylabs-mcp"
    else:
        raise ValueError(f"Unknown mcp server option: {MCP_SERVER}")

    async with MCPTools(
        command,
        env={
            "OXYLABS_USERNAME": os.getenv("OXYLABS_USERNAME"),
            "OXYLABS_PASSWORD": os.getenv("OXYLABS_PASSWORD"),
        },
    ) as mcp_server:
        yield mcp_server