# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/tool_handlers.py
# module: webEvalAgent.src.tool_handlers
# qname: webEvalAgent.src.tool_handlers.handle_web_evaluation
# lines: 43-197
async def handle_web_evaluation(arguments: Dict[str, Any], ctx: Context, api_key: str) -> list[TextContent]:
    """Handle web_eval_agent tool calls
    
    This function evaluates the user experience of a web application by using
    the browser-use agent to perform specific tasks and analyze the interaction flow.
    
    Args:
        arguments: The tool arguments containing 'url' and 'task'
        ctx: The MCP context for reporting progress
        api_key: The API key for authentication with the LLM service
        
    Returns:
        list[List[Any]]: The evaluation results, including console logs, network requests, and screenshots
    """
    # Initialize log server immediately (if not already running)
    try:
        # stop_log_server() # Commented out stop_log_server
        start_log_server()
        # Give the server a moment to start
        await asyncio.sleep(1)
        # Open the dashboard in a new tab
        open_log_dashboard()
    except Exception:
        pass
    
    # Validate required arguments
    if "url" not in arguments or "task" not in arguments:
        return [TextContent(
            type="text",
            text="Error: Both 'url' and 'task' parameters are required. Please provide a URL to evaluate and a specific UX/UI task to test."
        )]
    
    url = arguments["url"]
    task = arguments["task"]
    tool_call_id = arguments.get("tool_call_id", str(uuid.uuid4()))
    headless = arguments.get("headless", True)

    send_log(f"Handling web evaluation call with context: {ctx}", "🤔")

    
    # Ensure URL has a protocol (add https:// if missing)
    if not url.startswith(("http://", "https://", "file://", "data:", "chrome:", "javascript:")):
        url = "https://" + url
        send_log(f"Added https:// protocol to URL: {url}", "🔗")
    
    if not url or not isinstance(url, str):
        return [TextContent(
            type="text",
            text="Error: 'url' must be a non-empty string containing the web application URL to evaluate."
        )]
        
    if not task or not isinstance(task, str):
        return [TextContent(
            type="text",
            text="Error: 'task' must be a non-empty string describing the UX/UI aspect to test."
        )]
    
    # Send initial status to dashboard
    send_log(f"🚀 Received web evaluation task: {task}", "🚀")
    send_log(f"🔗 Target URL: {url}", "🔗")
    
    # Update the URL and task in the dashboard
    set_url_and_task(url, task)

    # Get the singleton browser manager and initialize it
    browser_manager = get_browser_manager()
    if not browser_manager.is_initialized:
        # Note: browser_manager.initialize will no longer need to start the log server
        # since we've already done it above
        await browser_manager.initialize()
        
    # Get the evaluation task prompt
    evaluation_task = get_web_evaluation_prompt(url, task)
    send_log("📝 Generated evaluation prompt.", "📝")
    
    # Run the browser task
    agent_result_data = None # Changed to agent_result_data
    try:
        # run_browser_task now returns a dictionary with result and screenshots # Updated comment
        agent_result_data = await run_browser_task(
            evaluation_task,
            headless=headless, # Pass the headless parameter
            tool_call_id=tool_call_id,
            api_key=api_key
        )
        
        # Extract the final result string
        agent_final_result = agent_result_data.get("result", "No result provided")
        screenshots = agent_result_data.get("screenshots", []) # Added this line

        # Log detailed screenshot information
        send_log(f"Received {len(screenshots)} screenshots from run_browser_task", "📸")
        for i, screenshot in enumerate(screenshots):
            if 'screenshot' in screenshot and screenshot['screenshot']:
                b64_length = len(screenshot['screenshot'])
                send_log(f"Processing screenshot {i+1}: Step {screenshot.get('step', 'unknown')}, {b64_length} base64 chars", "🔢")
            else:
                send_log(f"Screenshot {i+1} missing 'screenshot' data! Keys: {list(screenshot.keys())}", "⚠️")

        # Log the number of screenshots captured
        send_log(f"📸 Captured {len(screenshots)} screenshots during evaluation", "📸")

    except Exception as browser_task_error:
        error_msg = f"Error during browser task execution: {browser_task_error}\n{traceback.format_exc()}"
        send_log(error_msg, "❌")
        agent_final_result = f"Error: {browser_task_error}" # Provide error as result
        screenshots = [] # Ensure screenshots is defined even on error

    # Format the agent result in a more user-friendly way, including console and network errors
    formatted_result = format_agent_result(agent_final_result, url, task, console_log_storage, network_request_storage)
    
    # Determine if the task was successful
    task_succeeded = True
    if agent_final_result.startswith("Error:"):
        task_succeeded = False
    elif "success=False" in agent_final_result and "is_done=True" in agent_final_result:
        task_succeeded = False
    
    # Use appropriate status emoji
    status_emoji = "✅" if task_succeeded else "❌"
    
    # Return a better formatted message to the MCP user
    # Including a reference to the dashboard for detailed logs
    confirmation_text = f"{formatted_result}\n\n👁️ See the 'Operative Control Center' dashboard for detailed live logs.\nWeb Evaluation completed!"
    send_log(f"Web evaluation task completed for {url}.", status_emoji) # Also send confirmation to dashboard
    
    # Log final screenshot count before constructing response
    send_log(f"Constructing final response with {len(screenshots)} screenshots", "🧩")
    
    # Create the final response structure
    response = [TextContent(type="text", text=confirmation_text)]
    
    # Debug the screenshot data structure one last time before adding to response
    for i, screenshot_data in enumerate(screenshots[1:]):
        if 'screenshot' in screenshot_data and screenshot_data['screenshot']:
            b64_length = len(screenshot_data['screenshot'])
            send_log(f"Adding screenshot {i+1} to response ({b64_length} chars)", "➕")
            response.append(ImageContent(
                type="image",
                data=screenshot_data["screenshot"],
                mimeType="image/jpeg"
            ))
        else:
            send_log(f"Screenshot {i+1} can't be added to response - missing data!", "❌")
    
    send_log(f"Final response contains {len(response)} items ({len(response)-1} images)", "📦")
    
    # MCP tool function expects list[list[TextContent, ImageContent]] - see docstring in mcp_server.py
    send_log(f"Returning wrapped response: list[ [{len(response)} items] ]", "🎁")
    
    # return [response]  # This structure may be incorrect
    
    # The correct structure based on docstring is list[list[TextContent, ImageContent]]
    # i.e., a list containing a single list of mixed content items
    return [response]