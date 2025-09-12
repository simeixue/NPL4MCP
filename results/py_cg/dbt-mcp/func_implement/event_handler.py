# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/examples/pydantic_ai_agent/main.py
# module: examples.pydantic_ai_agent.main
# qname: examples.pydantic_ai_agent.main.main.event_handler
# lines: 49-54
                async def event_handler(ctx: RunContext, event_stream):
                    async for event in event_stream:
                        if isinstance(event, FunctionToolCallEvent):
                            print(f"\n🔧 Tool called: {event.part.tool_name}")
                            print(f"   Arguments: {event.part.args}")
                            print("Assistant: ", end="", flush=True)