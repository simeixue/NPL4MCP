# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/evals/semantic_layer/test_eval_semantic_layer.py
# module: evals.semantic_layer.test_eval_semantic_layer
# qname: evals.semantic_layer.test_eval_semantic_layer.expect_metadata_tool_call
# lines: 27-59
async def expect_metadata_tool_call(
    messages: list,
    tools: list[FunctionToolParam],
    expected_tool: str,
    expected_arguments: str | None = None,
) -> ResponseOutputItem:
    response = llm_client.responses.create(
        model=LLM_MODEL,
        input=messages,
        tools=tools,
        parallel_tool_calls=False,
    )
    assert len(response.output) == 1
    tool_call = response.output[0]
    assert isinstance(tool_call, ResponseFunctionToolCall)
    function_name = tool_call.name
    function_arguments = tool_call.arguments
    assert tool_call.type == "function_call"
    assert function_name == expected_tool
    assert expected_arguments is None or function_arguments == expected_arguments
    tool_response = await (await create_dbt_mcp(config)).call_tool(
        function_name,
        json.loads(function_arguments),
    )
    messages.append(tool_call)
    messages.append(
        FunctionCallOutput(
            type="function_call_output",
            call_id=tool_call.call_id,
            output=str(tool_response),
        )
    )
    return tool_call