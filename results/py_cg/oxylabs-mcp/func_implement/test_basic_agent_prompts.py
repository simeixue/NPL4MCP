# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/tests/e2e/test_llm_agent.py
# module: tests.e2e.test_llm_agent
# qname: tests.e2e.test_llm_agent.test_basic_agent_prompts
# lines: 145-164
async def test_basic_agent_prompts(
    model: str,
    query: str,
    tool: str,
    arguments: dict,
    expected_content: str,
):
    async with oxylabs_mcp_server() as mcp_server:
        agent = get_agent(model, mcp_server)
        response = await agent.arun(query)

    tool_calls = agent.memory.get_tool_calls(agent.session_id)

    # [tool_call, tool_call_result]
    assert len(tool_calls) == 2, "Extra tool calls found!"

    assert tool_calls[0]["function"]["name"] == tool
    assert json.loads(tool_calls[0]["function"]["arguments"]) == arguments

    assert expected_content in response.content