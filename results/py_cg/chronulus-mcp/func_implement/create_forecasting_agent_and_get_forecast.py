# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/chronulus-mcp/src/chronulus_mcp/agent/forecaster.py
# module: src.chronulus_mcp.agent.forecaster
# qname: src.chronulus_mcp.agent.forecaster.create_forecasting_agent_and_get_forecast
# lines: 16-103
async def create_forecasting_agent_and_get_forecast(
        session_id: Annotated[str, Field(description="The session_id for the forecasting or prediction use case")],
        input_data_model: Annotated[List[InputField], Field(
            description="""Metadata on the fields you will include in the input_data."""
        )],
        input_data: Annotated[Dict[str, Union[str, dict, List[dict]]], Field(description="The forecast inputs that you will pass to the chronulus agent to make the prediction. The keys of the dict should correspond to the InputField name you provided in input_fields.")],
        forecast_start_dt_str: Annotated[str, Field(description="The datetime str in '%Y-%m-%d %H:%M:%S' format of the first value in the forecast horizon.")],
        ctx: Context,
        time_scale: Annotated[str, Field(description="The times scale of the forecast horizon. Valid time scales are 'hours', 'days', and 'weeks'.", default="days")],
        horizon_len: Annotated[int, Field(description="The integer length of the forecast horizon. Eg., 60 if a 60 day forecast was requested.", default=60)],
) -> Union[str, Dict[str, Union[dict, str]]]:
    """Queues and retrieves a forecast from Chronulus with a predefined session_id

    This tool creates a NormalizedForecaster agent and then provides a forecast input to the agent and returns the prediction data and
    text explanation from the agent.

    Args:
        session_id (str): The session_id for the forecasting or prediction use case.
        input_data_model (List[InputField]): Metadata on the fields you will include in the input_data. Eg., for a field named "brand", add a description like "the brand of the product to forecast"
        input_data (Dict[str, Union[str, dict, List[dict]]]): The forecast inputs that you will pass to the chronulus agent to make the prediction. The keys of the dict should correspond to the InputField name you provided in input_fields.
        forecast_start_dt_str (str): The datetime str in '%Y-%m-%d %H:%M:%S' format of the first value in the forecast horizon."
        ctx (Context): Context object providing access to MCP capabilities.
        time_scale (str): The times scale of the forecast horizon. Valid time scales are 'hours', 'days', and 'weeks'.
        horizon_len (int): The integer length of the forecast horizon. Eg., 60 if a 60 day forecast was requested.

    Returns:
        Union[str, Dict[str, Union[dict, str]]]: a dictionary with prediction data, a text explanation of the predictions, estimator_id, and the prediction id.
    """


    try:
        chronulus_session = Session.load_from_saved_session(session_id=session_id, verbose=False)
    except Exception as e:
        error_message = f"Failed to retrieve session with session_id: {session_id}\n\n{e}"
        _ = await ctx.error( message=error_message)
        return error_message

    try:
        InputItem = generate_model_from_fields("InputItem", input_data_model)
    except Exception as e:
        error_message = f"Failed to create InputItem model with input data model: {json.dumps(input_data_model, indent=2)}\n\n{e}"
        _ = await ctx.error(message=error_message)
        return error_message

    try:
        item = InputItem(**input_data)
    except Exception as e:
        error_message = f"Failed to validate the input_data with the generated InputItem model. \n\n{e}"
        _ = await ctx.error(message=error_message)
        return error_message

    try:
        nf_agent = NormalizedForecaster(
            session=chronulus_session,
            input_type=InputItem,
            verbose=False,
        )
    except Exception as e:
        return f"""Error at nf_agent: {str(e)}
        
input_fields = {input_data_model}

input_data = {json.dumps(input_data, indent=2)}

input_type = {str(type(InputItem))}
"""

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