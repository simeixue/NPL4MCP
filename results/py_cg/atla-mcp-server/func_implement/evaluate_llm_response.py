# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/atla-mcp-server/atla_mcp_server/server.py
# module: atla_mcp_server.server
# qname: atla_mcp_server.server.evaluate_llm_response
# lines: 167-199
async def evaluate_llm_response(
    ctx: Context,
    evaluation_criteria: AnnotatedEvaluationCriteria,
    llm_prompt: AnnotatedLlmPrompt,
    llm_response: AnnotatedLlmResponse,
    expected_llm_output: AnnotatedExpectedLlmOutput = None,
    llm_context: AnnotatedLlmContext = None,
    model_id: AnnotatedModelId = "atla-selene",
) -> dict[str, str]:
    """Evaluate an LLM's response to a prompt using a given evaluation criteria.

    This function uses an Atla evaluation model under the hood to return a dictionary
    containing a score for the model's response and a textual critique containing
    feedback on the model's response.

    Returns:
        dict[str, str]: A dictionary containing the evaluation score and critique, in
            the format `{"score": <score>, "critique": <critique>}`.
    """
    state = cast(MCPState, ctx.request_context.lifespan_context)
    result = await state.atla_client.evaluation.create(
        model_id=model_id,
        model_input=llm_prompt,
        model_output=llm_response,
        evaluation_criteria=evaluation_criteria,
        expected_model_output=expected_llm_output,
        model_context=llm_context,
    )

    return {
        "score": result.result.evaluation.score,
        "critique": result.result.evaluation.critique,
    }