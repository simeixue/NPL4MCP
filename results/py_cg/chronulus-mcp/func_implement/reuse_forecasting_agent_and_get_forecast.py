# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/chronulus-mcp/src/chronulus_mcp/agent/forecaster.py
# module: src.chronulus_mcp.agent.forecaster
# qname: src.chronulus_mcp.agent.forecaster.reuse_forecasting_agent_and_get_forecast
# lines: 106-158
async def reuse_forecasting_agent_and_get_forecast(
        agent_id: Annotated[str, Field(description="The agent_id for the forecasting or prediction use case and previously defined input_data_model")],
        input_data: Annotated[Dict[str, Union[str, dict, List[dict]]], Field(
            description="The forecast inputs that you will pass to the chronulus agent to make the prediction. The keys of the dict should correspond to the InputField name you provided in input_fields.")],
        forecast_start_dt_str: Annotated[str, Field(
            description="The datetime str in '%Y-%m-%d %H:%M:%S' format of the first value in the forecast horizon.")],
        time_scale: Annotated[str, Field(
            description="The times scale of the forecast horizon. Valid time scales are 'hours', 'days', and 'weeks'.",
            default="days")],
        horizon_len: Annotated[int, Field(
            description="The integer length of the forecast horizon. Eg., 60 if a 60 day forecast was requested.",
            default=60)],
) -> Union[str, Dict[str, Union[dict, str]]]:
    """Queues and retrieves a forecast from Chronulus with a previously created agent_id

    This tool provides a forecast input to a previous created Chronulus NormalizedForecaster agent and returns the
    prediction data and text explanation from the agent.

    Args:
        agent_id (str): The agent_id for the forecasting or prediction use case and previously defined input_data_model
        input_data (Dict[str, Union[str, dict, List[dict]]]): The forecast inputs that you will pass to the chronulus agent to make the prediction. The keys of the dict should correspond to the InputField name you provided in input_fields.
        forecast_start_dt_str (str): The datetime str in '%Y-%m-%d %H:%M:%S' format of the first value in the forecast horizon."
        time_scale (str): The times scale of the forecast horizon. Valid time scales are 'hours', 'days', and 'weeks'.
        horizon_len (int): The integer length of the forecast horizon. Eg., 60 if a 60 day forecast was requested.

    Returns:
        Union[str, Dict[str, Union[dict, str]]]: a dictionary with prediction data, a text explanation of the predictions, agent_id, and the prediction id.
    """

    nf_agent = NormalizedForecaster.load_from_saved_estimator(estimator_id=agent_id, verbose=False)
    item = nf_agent.input_type(**input_data)

    try:
        forecast_start_dt = datetime.fromisoformat(forecast_start_dt_str)
        horizon_params = {
            'start_dt': forecast_start_dt,
            time_scale: horizon_len
        }
        req = nf_agent.queue(item, **horizon_params)
    except Exception as e:
        return f"""Error at nf_agent: {str(e)}"""

    try:
        predictions = nf_agent.get_predictions(req.request_id)
        prediction = predictions[0]
        return {
            "agent_id": nf_agent.estimator_id,
            "prediction_id": prediction.id,
            'data': prediction.to_json(orient='rows'),
            'explanation': prediction.text}

    except Exception as e:
        return f"""Error on prediction: {str(e)}"""