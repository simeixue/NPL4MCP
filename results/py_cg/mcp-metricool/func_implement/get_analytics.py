# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-metricool/src/mcp_metricool/tools/tools.py
# module: src.mcp_metricool.tools.tools
# qname: src.mcp_metricool.tools.tools.get_analytics
# lines: 708-814
async def get_analytics(blog_id: int, start: str, end: str, timezone: str, network: str, metric: [str]) -> str | dict[str, Any]:

    """
    Retrieve analytics data for a specific Metricool brand. If the user does not specify any metric you can use the
    get_metrics tool and let the user decide them.

    Args:
        - blog_id (int): ID of the Metricool brand account. Required.
        - start (str): Start date of the data period (format: YYYY-MM-DD). Required.
        - end (str): End date of the data period (format: YYYY-MM-DD). Required.
        - timezone (str): Timezone from the brand(e.g., Europe%2FMadrid). Required. If you don't have the timezone you can obtain it from the get_brands tool
        - network (str): Social network to analyze (e.g., facebook, instagram, linkedin, youtube, tiktok, etc.), it must be connected to the brand. Required.
        - metric ([str]): List of metrics, default is empty.
        If blog_id is missing, ask the user to provide it.
        If network is missing, ask the user to specify one.
        If network is not connected to the brand, ask the user to specify one of the connected ones.
"""

    if network not in network_subject_metrics:
        return f"Incorrect network '{network}'. The available networks are: {', '.join(network_subject_metrics.keys())}"
    if not metric:
        return "Please provide a list of metrics. You can use the 'get_metrics' tool to explore available metrics."

    results = {}


    subjects = list(network_subject_metrics[network].keys())
    start_formatted = format_datetime_with_timezone(start, "00:00:00", timezone)
    end_formatted = format_datetime_with_timezone(end, "23:59:59", timezone)
    start_aux = start.replace("-", "")
    end_aux = end.replace("-", "")
    for subj in subjects:
        metrics = metric if metric else network_subject_metrics[network][subj]
        for met in metrics:
            if met not in network_subject_metrics[network][subj]:
                continue
            if network == 'tiktok' and subj == 'videos':
                url = (
                f"{METRICOOL_BASE_URL}/v2/analytics/timelines"
                f"?blogId={blog_id}&userId={METRICOOL_USER_ID}&integrationSource=MCP"
                f"&from={start_formatted}&to={end_formatted}"
                f"&timezone={timezone}&metric={met}&network={network}"
                )
            elif network == 'youtube' and subj == 'videos':
                url = (
                    f"{METRICOOL_BASE_URL}/v2/analytics/timelines"
                    f"?blogId={blog_id}&userId={METRICOOL_USER_ID}&integrationSource=MCP"
                    f"&from={start_formatted}&to={end_formatted}"
                    f"&timezone={timezone}&metric={met}&network={network}&postsType=publishedInRange"
                )
            elif network == 'youtube' and subj == "account":
                url = (
                    f"https://app.metricool.com/api/stats/timeline/{met}?start={start_aux}&end={end_aux}&timezone={timezone}"
                    f"&userId={METRICOOL_USER_ID}&blogId={blog_id}&integrationSource=MCP"
                )
            elif network == "linkedin" and subj != "stories":
                url = (
                    f"{METRICOOL_BASE_URL}/v2/analytics/timelines"
                    f"?blogId={blog_id}&userId={METRICOOL_USER_ID}&integrationSource=MCP"
                    f"&from={start_formatted}&to={end_formatted}"
                    f"&timezone={timezone}&metric={met}&metricType={subj}&network={network}"
                )
            elif network == "linkedin" and subj == "stories":
                url = (
                    f"https://app.metricool.com/api/stats/timeline/{met}"
                    f"?start={start_aux}&end={end_aux}&userId={METRICOOL_USER_ID}&blogId={blog_id}&integrationSource=MCP"
                )
            elif network == "webpage":
                url = (
                    f"https://app.metricool.com/api/stats/timeline/{met}"
                    f"?start={start_aux}&end={end_aux}&userId={METRICOOL_USER_ID}&blogId={blog_id}&timezone={timezone}&integrationSource=MCP"
                )
            elif network == "twitter":
                url = (
                    f"https://app.metricool.com/api/stats/timeline/{met}"
                    f"?start={start_aux}&end={end_aux}&userId={METRICOOL_USER_ID}&blogId={blog_id}&timezone={timezone}&integrationSource=MCP"
                )
            elif network == "twitch":
                url = (
                    f"https://app.metricool.com/api/stats/timeline/twitch{met}"
                    f"?start={start_aux}&end={end_aux}&userId={METRICOOL_USER_ID}&blogId={blog_id}&timezone={timezone}&integrationSource=MCP"
                )
            else:
                url = (
                f"{METRICOOL_BASE_URL}/v2/analytics/timelines"
                f"?blogId={blog_id}&userId={METRICOOL_USER_ID}&integrationSource=MCP"
                f"&from={start_formatted}&to={end_formatted}"
                f"&timezone={timezone}&metric={met}&subject={subj}&network={network}"
                )
            try:
                result = await make_get_request(url)
                if result:
                    results[f"{subj}:{met}"] = result
                else:
                    results[f"{subj}:{met}"] = "No data"
            except Exception as e:
                results[f"{subj}:{met}"] = f"Error: {str(e)}"

            for key, value in results.items():
                if isinstance(value, dict) and "data" in value:
                    for item in value["data"]:
                        if isinstance(item, dict) and "values" in item:
                            for v in item["values"]:
                                if "dateTime" in v:
                                    v["dateTime"] = convert_datetime_to_timezone(v["dateTime"], unquote(timezone))

    return results if results else "No valid data."