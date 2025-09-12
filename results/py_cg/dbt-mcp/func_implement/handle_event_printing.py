# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/examples/openai_agent/main_streamable.py
# module: examples.openai_agent.main_streamable
# qname: examples.openai_agent.main_streamable.handle_event_printing
# lines: 29-43
def handle_event_printing(event, show_tools_calls=True):
    if type(event) is RunItemStreamEvent and show_tools_calls:
        if event.name == "tool_called":
            print_tool_call(
                event.item.raw_item.name,
                event.item.raw_item.arguments,
                color="grey",
                show_params=True,
            )

    if type(event) is RawResponsesStreamEvent:
        if type(event.data) is ResponseCompletedEvent:
            for output in event.data.response.output:
                if type(output) is ResponseOutputMessage:
                    print(output.content[0].text)