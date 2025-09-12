# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/chronulus-mcp/src/chronulus_mcp/io.py
# module: src.chronulus_mcp.io
# qname: src.chronulus_mcp.io.save_forecast
# lines: 16-61
async def save_forecast(
    prediction_id: Annotated[str, Field(description="The prediction_id from a prediction result")],
    output_path: Annotated[str, Field(description="The path where the CSV file should be saved. Should end in .csv")],
    csv_name: Annotated[str, Field(description="The path where the CSV file should be saved. Should end in .csv")],
    txt_name: Annotated[str, Field(description="The name of the TXT file to be saved. Should end in .txt")],
    ctx: Context,
    y_min: Annotated[float, Field(default=0.0, description="The expected smallest value for the use case. E.g., for product sales, 0 would be the least possible value for sales.")],
    y_max: Annotated[float, Field(default=1.0, description="The expected largest value for the use case. E.g., for product sales, 0 would be the largest possible value would be given by the user or determined from this history of sales for the product in question or a similar product.")],
    invert_scale: Annotated[bool, Field(default=False, description="Set this flag to true if the scale of the new units will run in the opposite direction from the inputs.")],
) -> str:
    """Saves the forecast from a NormalizedForecaster agent to CSV and the explanation to TXT

    Args:
        prediction_id (str): The prediction_id for the prediction you would like to rescale as returned by the forecasting agent
        output_path (str): The path where the CSV and TXT file should be saved.
        csv_name (str): The name of the CSV file to be saved. Should end in .csv
        txt_name (str): The name of the TXT file to be saved. Should end in .txt
        ctx (Context): Context object providing access to MCP capabilities.
        y_min (float): The expected smallest value for the use case. E.g., for product sales, 0 would be the least possible value for sales.
        y_max (float): The expected largest value for the use case. E.g., for product sales, 0 would be the largest possible value would be given by the user or determined from this history of sales for the product in question or a similar product.
        invert_scale (bool): Set this flag to true if the scale of the new units will run in the opposite direction from the inputs.


    Returns:
        str: A message confirming the file was saved and its location
    """
    # Get normalized forecast and rescale it
    _ = await ctx.info(f"Fetching prediction data for {prediction_id}")
    normalized_forecast = NormalizedForecaster.get_prediction_static(prediction_id, verbose=False)
    rescaled_forecast = RescaledForecast.from_forecast(
        forecast=normalized_forecast,
        y_min=y_min,
        y_max=y_max,
        invert_scale=invert_scale
    )

    # Convert to pandas using built-in method
    df = rescaled_forecast.to_pandas()

    # Save to CSV
    df.to_csv(os.path.join(output_path, csv_name), index_label="ds")

    with open(os.path.join(output_path, txt_name), "w") as f:
        f.write(normalized_forecast.text)

    return f"Forecast saved successfully to {output_path}"