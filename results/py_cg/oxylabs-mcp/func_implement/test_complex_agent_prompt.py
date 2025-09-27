# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/tests/e2e/test_llm_agent.py
# module: tests.e2e.test_llm_agent
# qname: tests.e2e.test_llm_agent.test_complex_agent_prompt
# lines: 169-192
async def test_complex_agent_prompt(model: str):
    async with oxylabs_mcp_server() as mcp_server:
        agent = get_agent(model, mcp_server)

        await agent.arun(
            "Go to oxylabs.io, look for career page, "
            "go to it and return all job titles in markdown format. "
            "Don't invent URLs, start from one provided."
        )

    tool_calls = agent.memory.get_tool_calls(agent.session_id)
    assert len(tool_calls) == 4, f"Not enough tool_calls, got {len(tool_calls)}: {tool_calls}"

    oxylabs_page_call, _, careers_page_call, _ = agent.memory.get_tool_calls(agent.session_id)
    assert oxylabs_page_call["function"]["name"] == "universal_scraper"
    assert json.loads(oxylabs_page_call["function"]["arguments"]) == {
        "output_format": "links",
        "url": "https://oxylabs.io",
    }
    assert careers_page_call["function"]["name"] == "universal_scraper"
    assert json.loads(careers_page_call["function"]["arguments"]) == {
        "output_format": "md",
        "url": "https://career.oxylabs.io/",
    }