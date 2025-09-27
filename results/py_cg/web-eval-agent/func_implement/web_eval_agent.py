# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/mcp_server.py
# module: webEvalAgent.mcp_server
# qname: webEvalAgent.mcp_server.web_eval_agent
# lines: 57-101
async def web_eval_agent(url: str, task: str, ctx: Context, headless_browser: bool = False) -> list[TextContent]:
    """Evaluate the user experience / interface of a web application.

    This tool allows the AI to assess the quality of user experience and interface design
    of a web application by performing specific tasks and analyzing the interaction flow.

    Before this tool is used, the web application should already be running locally on a port.

    Args:
        url: Required. The localhost URL of the web application to evaluate, including the port number.
            Example: http://localhost:3000, http://localhost:8080, http://localhost:4200, http://localhost:5173, etc.
            Try to avoid using the path segments of the URL, and instead use the root URL.
        task: Required. The specific UX/UI aspect to test (e.g., "test the checkout flow",
             "evaluate the navigation menu usability", "check form validation feedback")
             Be as detailed as possible in your task description. It could be anywhere from 2 sentences to 2 paragraphs.
        headless_browser: Optional. Whether to hide the browser window popup during evaluation.
        If headless_browser is True, only the operative control center browser will show, and no popup browser will be shown.

    Returns:
        list[list[TextContent, ImageContent]]: A detailed evaluation of the web application's UX/UI, including
                         observations, issues found, and recommendations for improvement
                         and screenshots of the web application during the evaluation
    """
    headless = headless_browser
    is_valid = await validate_api_key(api_key)

    if not is_valid:
        error_message_str = "❌ Error: API Key validation failed when running the tool.\n"
        error_message_str += "   Reason: Free tier limit reached.\n"
        error_message_str += "   👉 Please subscribe at https://operative.sh to continue."
        return [TextContent(type="text", text=error_message_str)]
    try:
        # Generate a new tool_call_id for this specific tool call
        tool_call_id = str(uuid.uuid4())
        return await handle_web_evaluation(
            {"url": url, "task": task, "headless": headless, "tool_call_id": tool_call_id},
            ctx,
            api_key
        )
    except Exception as e:
        tb = traceback.format_exc()
        return [TextContent(
            type="text",
            text=f"Error executing web_eval_agent: {str(e)}\n\nTraceback:\n{tb}"
        )]