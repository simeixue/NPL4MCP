# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/evals/semantic_layer/test_eval_semantic_layer.py
# module: evals.semantic_layer.test_eval_semantic_layer
# qname: evals.semantic_layer.test_eval_semantic_layer.test_explicit_tool_request
# lines: 165-175
async def test_explicit_tool_request(content: str, expected_tool: str):
    dbt_mcp = await create_dbt_mcp(config)
    response = llm_client.responses.create(
        model=LLM_MODEL,
        input=initial_messages(content),
        tools=await get_tools(dbt_mcp),
        parallel_tool_calls=False,
    )
    assert len(response.output) == 1
    assert response.output[0].type == "function_call"
    assert response.output[0].name == expected_tool