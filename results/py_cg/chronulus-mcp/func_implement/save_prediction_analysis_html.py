# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/chronulus-mcp/src/chronulus_mcp/io.py
# module: src.chronulus_mcp.io
# qname: src.chronulus_mcp.io.save_prediction_analysis_html
# lines: 65-148
async def save_prediction_analysis_html(
    request_id: Annotated[str, Field(description="The request_id from the BinaryPredictor result")],
    output_path: Annotated[str, Field(description="The path where the HTML file should be saved.")],
    html_name: Annotated[str, Field(description="The path where the HTML file should be saved.")],
    title: Annotated[str, Field(description="Title of analysis")],
    plot_label: Annotated[str, Field(description="Label for the Beta plot")],
    chronulus_prediction_summary: Annotated[str, Field(description="A summary paragraph distilling prediction results and expert opinions provided by Chronulus")],
    dist_shape: Annotated[str, Field(description="A one line description of the shape of the distribution of predictions")],
    dist_shape_interpretation: Annotated[str, Field(description="2-3 sentences interpreting the shape of the distribution of predictions in layman's terms")],
    #ctx: Context,
) -> str:
    """Saves the analysis from a BinaryPredictor prediction to an HTML file

    Args:
        request_id (str): The request_id from the BinaryPredictor result
        output_path (str): The path where the CSV and TXT file should be saved.
        html_name (str): The name of the HTML file to be saved. Should end in .html
        title (str): Title of analysis
        plot_label (str): Label for the Beta plot
        chronulus_prediction_summary (str) : A summary paragraph distilling prediction results and expert opinions provided by Chronulus
        dist_shape (str) : A one line description of the shape of the distribution of predictions
        dist_shape_interpretation (str) : A 2-3 sentences interpreting the shape of the distribution of predictions in layman's terms

    Returns:
        str: A message confirming the file was saved and its location
    """
    # Get normalized forecast and rescale it
    #_ = await ctx.info(f"Fetching prediction data for request_id: {request_id}")

    html = get_html_template("binary_predictor_analysis.html")

    prediction_set = BinaryPredictor.get_request_predictions_static(request_id, verbose=False)

    mean = prediction_set.prob_a
    a, b = prediction_set.beta_params.alpha, prediction_set.beta_params.beta
    variance = (a*b) / (((a+b)**2)*(a+b+1))
    stdev = math.sqrt(variance)
    divergent = a <= 1 or b <= 1
    mode = (a - 1) / (a + b - 2)
    mode_txt = f"{mode: 16.4f}" if not divergent else 'Diverges'

    html = html.replace("[TITLE_OF_ANALYSIS]", title)
    html = html.replace("[PLOT_LABEL]", plot_label)
    html = html.replace("[CHRONULUS_PREDICTION_SUMMARY]", chronulus_prediction_summary)
    html = html.replace("[DIST_SHAPE_DESCRIPTION]", dist_shape)
    html = html.replace("[DIST_SHAPE_INTERPRETATION]", dist_shape_interpretation)
    html = html.replace("[ALPHA]", f"{a: 16.16f}")
    html = html.replace("[BETA]", f"{b: 16.16f}")
    html = html.replace("[MEAN]", f"{mean: 16.4f}")
    html = html.replace("[VARIANCE]", f"{variance: 16.4f}")
    html = html.replace("[STDEV]", f"{stdev: 16.4f}")
    html = html.replace("[MODE]", mode_txt)

    date = datetime.today().strftime("%B %d, %Y")
    html = html.replace("[DATE]", date)

    expert_opinion_list = []
    for i, p in enumerate(prediction_set):
        pos_text = p.opinion_set.positive.text
        neg_text = p.opinion_set.negative.text
        pos = f"""
        <div class="expert-opinion positive-case">
            <h3>Expert {i+1} - Positive Case</h3>
                <pre>{pos_text}</pre>
        </div>
        """
        neg = f"""
        <div class="expert-opinion negative-case">
            <h3>Expert {i+1} - Negative Case</h3>
                <pre>{neg_text}</pre>
        </div>
        """
        expert_opinion_list.append(pos)
        expert_opinion_list.append(neg)

    expert_opinions = "\n\n".join(expert_opinion_list)

    html = html.replace("[EXPERT_OPINIONS]", expert_opinions)


    with open(os.path.join(output_path, html_name), "w") as f:
        f.write(html)

    return f"BinaryPredictor analysis saved successfully to {output_path}"