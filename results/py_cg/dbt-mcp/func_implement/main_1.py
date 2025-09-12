# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/examples/openai_agent/main_streamable.py
# module: examples.openai_agent.main_streamable
# qname: examples.openai_agent.main_streamable.main
# lines: 46-93
async def main(inspect_events_tools_calls=False):
    prod_environment_id = os.environ.get("DBT_PROD_ENV_ID", os.getenv("DBT_ENV_ID"))
    token = os.environ.get("DBT_TOKEN")
    host = os.environ.get("DBT_HOST", "cloud.getdbt.com")

    async with MCPServerStreamableHttp(
        name="dbt",
        params={
            "url": f"https://{host}/api/ai/v1/mcp/",
            "headers": {
                "Authorization": f"token {token}",
                "x-dbt-prod-environment-id": prod_environment_id,
            },
        },
        client_session_timeout_seconds=20,
        cache_tools_list=True,
        tool_filter=create_static_tool_filter(
            allowed_tool_names=[
                "list_metrics",
                "get_dimensions",
                "get_entities",
                "query_metrics",
                "get_metrics_compiled_sql",
            ],
        ),
    ) as server:
        agent = Agent(
            name="Assistant",
            instructions="Use the tools to answer the user's questions. Do not invent data or sample data.",
            mcp_servers=[server],
            model="gpt-5",
        )
        with trace(workflow_name="Conversation"):
            conversation = []
            result = None
            while True:
                if result:
                    conversation = result.to_input_list()
                conversation.append({"role": "user", "content": input("User > ")})

                if inspect_events_tools_calls:
                    async for event in Runner.run_streamed(
                        agent, conversation
                    ).stream_events():
                        handle_event_printing(event, show_tools_calls=True)
                else:
                    result = await Runner.run(agent, conversation)
                    print(result.final_output)