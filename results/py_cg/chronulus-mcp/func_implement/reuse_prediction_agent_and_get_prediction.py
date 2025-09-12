# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/chronulus-mcp/src/chronulus_mcp/agent/predictor.py
# module: src.chronulus_mcp.agent.predictor
# qname: src.chronulus_mcp.agent.predictor.reuse_prediction_agent_and_get_prediction
# lines: 95-134
async def reuse_prediction_agent_and_get_prediction(
        agent_id: Annotated[str, Field(description="The agent_id for the forecasting or prediction use case and previously defined input_data_model")],
        input_data: Annotated[Dict[str, Union[str, dict, List[dict]]], Field(
            description="The forecast inputs that you will pass to the chronulus agent to make the prediction. The keys of the dict should correspond to the InputField name you provided in input_fields.")],
        num_experts: Annotated[int, Field(description="The number of experts to consult when forming consensus")],

) -> Union[str, Dict[str, Union[dict, str]]]:
    """Queues and retrieves a binary event prediction from Chronulus with a previously created agent_id

    This tool provides a prediction input to a previous created Chronulus BinaryPredictor agent and returns the
    prediction data and text explanations from each of the experts consulted by the agent.

    Args:
        agent_id (str): The agent_id for the forecasting or prediction use case and previously defined input_data_model
        input_data (Dict[str, Union[str, dict, List[dict]]]): The forecast inputs that you will pass to the chronulus agent to make the prediction. The keys of the dict should correspond to the InputField name you provided in input_fields.
        num_experts (int): The number of experts to consult when forming consensus.

    Returns:
        Union[str, Dict[str, Union[dict, str]]]: a dictionary with prediction data, a text explanation of the predictions, agent_id, and probability estimate.
    """

    agent = BinaryPredictor.load_from_saved_estimator(estimator_id=agent_id, verbose=False)
    item = agent.input_type(**input_data)

    try:
        req = agent.queue(item, num_experts=num_experts, note_length=(5,10))
    except Exception as e:
        return f"""Error at nf_agent: {str(e)}"""

    try:
        prediction_set = agent.get_request_predictions(req.request_id)
        return {
            "agent_id": agent.estimator_id,
            "request_id": req.request_id,
            "beta_params": prediction_set.beta_params,
            'expert_opinions': [p.text for p in prediction_set],
            'probability': prediction_set.prob_a}

    except Exception as e:
        return f"""Error on prediction: {str(e)}"""