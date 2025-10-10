# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/atla-mcp-server/atla_mcp_server/server.py
# module: atla_mcp_server.server
# qname: atla_mcp_server.server.evaluate_llm_response_on_multiple_criteria
# lines: 202-236
async def evaluate_llm_response_on_multiple_criteria(
    ctx: Context,
    evaluation_criteria_list: list[AnnotatedEvaluationCriteria],
    llm_prompt: AnnotatedLlmPrompt,
    llm_response: AnnotatedLlmResponse,
    expected_llm_output: AnnotatedExpectedLlmOutput = None,
    llm_context: AnnotatedLlmContext = None,
    model_id: AnnotatedModelId = "atla-selene",
) -> list[dict[str, str]]:
    """Evaluate an LLM's response to a prompt across *multiple* evaluation criteria.

    This function uses an Atla evaluation model under the hood to return a list of
    dictionaries, each containing an evaluation score and critique for a given
    criteria.

    Returns:
        list[dict[str, str]]: A list of dictionaries containing the evaluation score
            and critique, in the format `{"score": <score>, "critique": <critique>}`.
            The order of the dictionaries in the list will match the order of the
            criteria in the `evaluation_criteria_list` argument.
    """
    tasks = [
        evaluate_llm_response(
            ctx=ctx,
            evaluation_criteria=criterion,
            llm_prompt=llm_prompt,
            llm_response=llm_response,
            expected_llm_output=expected_llm_output,
            llm_context=llm_context,
            model_id=model_id,
        )
        for criterion in evaluation_criteria_list
    ]
    results = await asyncio.gather(*tasks)
    return results