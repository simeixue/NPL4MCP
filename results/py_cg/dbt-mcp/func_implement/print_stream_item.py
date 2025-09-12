# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/examples/langgraph_agent/main.py
# module: examples.langgraph_agent.main
# qname: examples.langgraph_agent.main.print_stream_item
# lines: 11-28
def print_stream_item(item):
    if "agent" in item:
        content = [
            part
            for message in item["agent"]["messages"]
            for part in (
                message.content
                if isinstance(message.content, list)
                else [message.content]
            )
        ]
        for c in content:
            if isinstance(c, str):
                print(f"Agent > {c}")
            elif "text" in c:
                print(f"Agent > {c['text']}")
            elif c["type"] == "tool_use":
                print(f"    using tool: {c['name']}")