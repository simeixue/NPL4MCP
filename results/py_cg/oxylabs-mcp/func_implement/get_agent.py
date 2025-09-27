# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/tests/e2e/test_llm_agent.py
# module: tests.e2e.test_llm_agent
# qname: tests.e2e.test_llm_agent.get_agent
# lines: 19-32
def get_agent(model: str, oxylabs_mcp: MCPTools) -> Agent:
    if model == "gemini":
        model_ = Gemini(api_key=os.getenv("GOOGLE_API_KEY"))
    elif model == "openai":
        model_ = OpenAIChat(api_key=os.getenv("OPENAI_API_KEY"))
    else:
        raise ValueError(f"Unknown model: {model}")

    return Agent(
        model=model_,
        tools=[oxylabs_mcp],
        instructions=["Use MCP tools to fulfil the requests"],
        markdown=True,
    )