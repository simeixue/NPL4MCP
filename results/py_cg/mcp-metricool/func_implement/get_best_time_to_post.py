# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-metricool/src/mcp_metricool/tools/tools.py
# module: src.mcp_metricool.tools.tools
# qname: src.mcp_metricool.tools.tools.get_best_time_to_post
# lines: 580-615
async def get_best_time_to_post(start: str, end: str, blog_id: int, provider: str, timezone: str) -> str | dict[
    str, Any]:
    """
    Get the best time to post for a specific provider. The return is a list of hours and days with a value. The higher the value, the best time to post.
    Try to get the best for as maximum of 1 week. If you have day to publish but not hours, choose the start and end of this day.
    Args:
     start: Start date of the period to get the data. The format is YYYY-MM-DD
     end: End date of the period to get the data. The format is YYYY-MM-DD
     blog id: Blog id of the Metricool brand account.
     provider: Provider of the post. The format is "twitter", "facebook", "instagram", "linkedin", "youtube", "tiktok". Only these are accepted.
     timezone: Timezone of the post. The format is "Europe%2FMadrid".  Use the timezone of the user extracted from the get_brands tool.
    """

    days_of_week = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }

    url = f"{METRICOOL_BASE_URL}/v2/scheduler/besttimes/{provider}?start={start}T00%3A00%3A00&end={end}T23%3A59%3A59&timezone={timezone}&blogId={blog_id}&userId={METRICOOL_USER_ID}&integrationSource=MCP"

    response = await make_get_request(url)

    if not response:
        return ("Failed to get the best time to post")

    #Introducir día de la semana
    for entry in response["data"]:
        day_number = entry.get("dayOfWeek")
        entry["dayOfWeekName"] = days_of_week.get(day_number, "Unknown")

    return response