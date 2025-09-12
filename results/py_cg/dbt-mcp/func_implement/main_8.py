# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/client/main.py
# module: src.client.main
# qname: src.client.main.main
# lines: 21-91
async def main():
    dbt_mcp = await create_dbt_mcp(config)
    user_role = "user"
    available_tools = await get_tools(dbt_mcp)
    tools_str = "\n".join(
        [
            f"- {t['name']}({', '.join(t['parameters']['properties'].keys())})"
            for t in available_tools
        ]
    )
    print(f"Available tools:\n{tools_str}")
    while True:
        user_input = input(f"{user_role} > ")
        messages.append({"role": user_role, "content": user_input})
        response_output = None
        tool_call_error = None
        while (
            response_output is None
            or response_output.type == "function_call"
            or tool_call_error is not None
        ):
            tool_call_error = None
            response = llm_client.responses.create(
                model=LLM_MODEL,
                input=messages,
                tools=available_tools,
                parallel_tool_calls=False,
            )
            response_output = response.output[0]
            if isinstance(response_output, ResponseOutputMessage):
                print(f"{response_output.role} > {response_output.content[0].text}")
            messages.append(response_output)
            if response_output.type != "function_call":
                continue
            print(
                f"Calling tool: {response_output.name} with arguments: {response_output.arguments}"
            )
            start_time = time()
            try:
                tool_response = await dbt_mcp.call_tool(
                    response_output.name,
                    json.loads(response_output.arguments),
                )
            except Exception as e:
                tool_call_error = e
                print(f"Error calling tool: {e}")
                messages.append(
                    FunctionCallOutput(
                        type="function_call_output",
                        call_id=response_output.call_id,
                        output=str(e),
                    )
                )
                continue
            tool_response_str = str(tool_response)
            print(
                f"Tool responded in {time() - start_time} seconds: "
                + (
                    f"{tool_response_str[:TOOL_RESPONSE_TRUNCATION]} [TRUNCATED]..."
                    if TOOL_RESPONSE_TRUNCATION
                    and len(tool_response_str) > TOOL_RESPONSE_TRUNCATION
                    else tool_response_str
                )
            )
            messages.append(
                FunctionCallOutput(
                    type="function_call_output",
                    call_id=response_output.call_id,
                    output=str(tool_response),
                )
            )