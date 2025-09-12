# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/examples/langgraph_agent/main.py
# module: examples.langgraph_agent.main
# qname: examples.langgraph_agent.main.main
# lines: 31-63
async def main():
    url = f"https://{os.environ.get('DBT_HOST')}/api/ai/v1/mcp/"
    headers = {
        "x-dbt-user-id": os.environ.get("DBT_USER_ID"),
        "x-dbt-prod-environment-id": os.environ.get("DBT_PROD_ENV_ID"),
        "x-dbt-dev-environment-id": os.environ.get("DBT_DEV_ENV_ID"),
        "Authorization": f"token {os.environ.get('DBT_TOKEN')}",
    }
    client = MultiServerMCPClient(
        {
            "dbt": {
                "url": url,
                "headers": headers,
                "transport": "streamable_http",
            }
        }
    )
    tools = await client.get_tools()
    agent = create_react_agent(
        model="anthropic:claude-3-7-sonnet-latest",
        tools=tools,
        # This allows the agent to have conversational memory.
        checkpointer=InMemorySaver(),
    )
    # This config maintains the conversation thread.
    config = {"configurable": {"thread_id": "1"}}
    while True:
        user_input = input("User > ")
        async for item in agent.astream(
            {"messages": {"role": "user", "content": user_input}},
            config,
        ):
            print_stream_item(item)