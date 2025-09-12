# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/chronulus-mcp/src/chronulus_mcp/agent/forecaster.py
# module: src.chronulus_mcp.agent.forecaster
# qname: src.chronulus_mcp.agent.forecaster.rescale_forecast
# lines: 161-187
async def rescale_forecast(
    prediction_id: Annotated[str, Field(description="The prediction_id from a prediction result")],
    y_min: Annotated[float, Field(description="The expected smallest value for the use case. E.g., for product sales, 0 would be the least possible value for sales.")],
    y_max: Annotated[float, Field(description="The expected largest value for the use case. E.g., for product sales, 0 would be the largest possible value would be given by the user or determined from this history of sales for the product in question or a similar product.")],
    invert_scale: Annotated[bool, Field(description="Set this flag to true if the scale of the new units will run in the opposite direction from the inputs.", default=False)],
) -> List[dict]:
    """Rescales prediction data from the NormalizedForecaster agent

    Args:
        prediction_id (str) : The prediction_id for the prediction you would like to rescale as returned by the forecasting agent
        y_min (float) : The expected smallest value for the use case. E.g., for product sales, 0 would be the least possible value for sales.
        y_max (float) : The expected largest value for the use case. E.g., for product sales, 0 would be the largest possible value would be given by the user or determined from this history of sales for the product in question or a similar product.
        invert_scale (bool): Set this flag to true if the scale of the new units will run in the opposite direction from the inputs.

    Returns:
        List[dict] : The prediction data rescaled to suit the use case
    """

    normalized_forecast = NormalizedForecaster.get_prediction_static(prediction_id)
    rescaled_forecast = RescaledForecast.from_forecast(
        forecast=normalized_forecast,
        y_min=y_min,
        y_max=y_max,
        invert_scale=invert_scale
    )

    return [DataRow(dt=row.get('date',row.get('datetime')), y_hat=row.get('y_hat')).model_dump() for row in rescaled_forecast.to_json(orient='rows')]