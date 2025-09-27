# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils.run_browser_task
# lines: 739-1277
async def run_browser_task(
    task: str, tool_call_id: str = None, api_key: str = None, headless: bool = True
) -> Dict[str, Any]:
    global browser_task_loop, screenshot_task
    # Store the current asyncio loop for input handling
    browser_task_loop = asyncio.get_running_loop()
    """
    Run a task using browser-use agent, sending logs to the dashboard.

    Args:
        task: The task to run.
        tool_call_id: The tool call ID for API headers.
        api_key: The API key for authentication.

    Returns:
        str: Agent's final result (stringified).
    """
    global \
        agent_instance, \
        console_log_storage, \
        network_request_storage, \
        screenshot_storage, \
        original_create_context, \
        _original_bring_to_front
    global active_cdp_session, active_screencast_running

    # Clear screenshot storage for this run
    screenshot_storage.clear()
    import traceback  # Make sure traceback is imported for error logging

    # --- Clear Logs for this Run ---
    console_log_storage.clear()
    network_request_storage.clear()

    # Local Playwright variables for this run
    playwright = None
    playwright_browser = None
    agent_browser = None  # browser-use Browser instance
    local_original_create_context = (
        None  # To store original method for this run's finally block
    )

    # Configure logging suppression
    logging.basicConfig(level=logging.CRITICAL)  # Set root logger level first
    # Then configure specific loggers
    for logger_name in ["browser_use", "root", "agent", "browser"]:
        # Get the logger for the current name and set its level
        current_logger = logging.getLogger(logger_name)
        current_logger.setLevel(logging.CRITICAL)

    warnings.filterwarnings("ignore", category=UserWarning)
    set_verbose(False)

    try:
        # Apply the patch to prevent focus stealing
        global _original_bring_to_front
        _original_bring_to_front = PlaywrightPage.bring_to_front
        PlaywrightPage.bring_to_front = _no_bring_to_front

        # --- Initialize Playwright Directly ---
        playwright = await async_playwright().start()
        # Launch with CDP enabled
        playwright_browser = await playwright.chromium.launch(
            headless=headless,  # Use the provided headless parameter
            args=["--remote-debugging-port=9222"],
        )

        # Get the CDP URL from the browser
        send_log(
            f"Playwright initialized for task with CDP (headless={headless}).",
            "🎭",
            log_type="status",
        )  # Type: status

        # --- Check for persisted browser state ---
        persisted_state = _get_persisted_state()
        if persisted_state:
            send_log(
                f"Loading persisted browser state from {persisted_state}",
                "💾",
                log_type="status",
            )

        # --- Create browser-use Browser ---
        browser_config = BrowserConfig(
            disable_security=True, headless=headless, cdp_url="http://127.0.0.1:9222"
        )
        agent_browser = Browser(config=browser_config)
        agent_browser.playwright = playwright
        agent_browser.playwright_browser = playwright_browser
        send_log(
            "Linked Playwright to agent browser with CDP enabled.",
            "🔗",
            log_type="status",
        )  # Type: status

        # --- Set up CDP screencasting ---
        # Detailed logging and error handling for each step
        try:
            # Create a context and page as recommended
            context = await playwright_browser.new_context(
                storage_state=persisted_state
            )
            first_page = await context.new_page()

            # Create a CDP session for the page
            try:
                cdp_session = await context.new_cdp_session(first_page)
                # Store the CDP session globally for input handling
                global active_cdp_session
                active_cdp_session = cdp_session
            except Exception as cdp_error:
                send_log(
                    f"Failed to create CDP session: {cdp_error}",
                    "❌",
                    log_type="status",
                )
                import traceback

                raise  # Re-raise to be caught by outer try/except

            # Set up a listener for screencast frames
            async def handle_screencast_frame(params):
                if "data" not in params:
                    return

                if "sessionId" not in params:
                    return

                try:
                    # Format as data URL
                    image_data = params["data"]
                    image_data_url = f"data:image/jpeg;base64,{image_data}"

                    # Send to frontend via SocketIO
                    try:
                        from .log_server import send_browser_view
                    except ImportError:
                        return

                    try:
                        await send_browser_view(image_data_url)
                    except Exception:
                        pass

                    # Acknowledge the frame
                    try:
                        await cdp_session.send(
                            "Page.screencastFrameAck",
                            {"sessionId": params["sessionId"]},
                        )
                    except Exception:
                        pass
                except Exception:
                    pass

            # Define async wrapper function for screencast frame event
            cdp_session.on("Page.screencastFrame", handle_screencast_frame)

            # Start the screencast
            try:
                await cdp_session.send(
                    "Page.startScreencast",
                    {
                        "format": "png",
                        "quality": 100,
                        "maxWidth": 1920,
                        "maxHeight": 1080,
                    },
                )
            except Exception as start_error:
                send_log(
                    f"Failed to start screencast: {start_error}",
                    "❌",
                    log_type="status",
                )
                import traceback

                raise  # Re-raise to be caught by outer try/except

            # Test if we can take a screenshot directly
            try:
                screenshot_bytes = await first_page.screenshot(type="jpeg")

                # Try sending this screenshot directly
                import base64

                screenshot_b64 = base64.b64encode(screenshot_bytes).decode("utf-8")
                direct_image_url = f"data:image/jpeg;base64,{screenshot_b64}"

                from .log_server import send_browser_view

                await send_browser_view(direct_image_url)
            except Exception:
                import traceback

            send_log(
                "CDP screencast started for browser-use browser.",
                "📹",
                log_type="status",
            )

            # Define the periodic screenshot capture function
            async def capture_screenshots(page, interval=1 / 30):
                """Capture screenshots at the specified interval in seconds (30 FPS)."""
                global active_screencast_running
                send_log(
                    "Starting periodic screenshot capture at 30 FPS",
                    "🎬",
                    log_type="status",
                )
                try:
                    while active_screencast_running:
                        try:
                            # Take a screenshot
                            screenshot_bytes = await page.screenshot(
                                type="jpeg", quality=80
                            )

                            # Convert to base64
                            screenshot_b64 = base64.b64encode(screenshot_bytes).decode(
                                "utf-8"
                            )

                            # Format as data URL
                            screenshot_data_url = (
                                f"data:image/jpeg;base64,{screenshot_b64}"
                            )

                            # Send to frontend
                            from .log_server import send_browser_view

                            await send_browser_view(screenshot_data_url)

                        except Exception as e:
                            if not active_screencast_running:
                                break
                            # Don't log every error to avoid spamming
                            if (
                                "Target closed" in str(e)
                                or "Session closed" in str(e)
                                or "Connection closed" in str(e)
                            ):
                                active_screencast_running = False
                                break

                        # Wait for the next interval
                        await asyncio.sleep(interval)
                except asyncio.CancelledError:
                    send_log(
                        "Periodic screenshot capture stopped", "🛑", log_type="status"
                    )
                except Exception as e:
                    send_log(f"Screenshot capture error: {e}", "❌", log_type="status")

            # Start the screenshot capture task
            active_screencast_running = True
            if headless:
                screenshot_task = asyncio.create_task(capture_screenshots(first_page))

        except Exception as e:
            send_log(f"Failed to start CDP screencast: {e}", "❌", log_type="status")
            import traceback

        # --- Patch BrowserContext._create_context ---
        # Store original only if not already stored (first run)
        if original_create_context is None:
            original_create_context = BrowserContext._create_context
            local_original_create_context = (
                original_create_context  # Also store for finally block
            )
        else:
            # Already patched, just ensure we have a reference for finally
            local_original_create_context = original_create_context

        async def patched_create_context(self, browser_pw):
            if original_create_context is None:
                raise RuntimeError("Original _create_context not stored correctly")

            # Check for persisted browser state
            persisted_state = _get_persisted_state()
            if persisted_state:
                send_log(
                    "Loading persisted browser state in new context",
                    "💾",
                    log_type="status",
                )

            # Call the original method but with storage_state if available
            raw_playwright_context = await original_create_context(self, browser_pw)

            # Apply storage state after context creation if available
            if persisted_state and raw_playwright_context:
                try:
                    with open(persisted_state, "r") as f:
                        state_data = json.load(f)

                    # Load cookies and localStorage from state
                    if "cookies" in state_data:
                        await raw_playwright_context.add_cookies(state_data["cookies"])

                    # Origins with storage set is already handled by Playwright internally
                    send_log(
                        "Applied persisted browser state to context",
                        "💾",
                        log_type="status",
                    )
                except Exception as e:
                    send_log(
                        f"Failed to apply persisted state to context: {e}",
                        "⚠️",
                        log_type="status",
                    )

            if raw_playwright_context:
                # Use the non-async wrapper functions for event listeners
                raw_playwright_context.on("console", handle_console_message)
                raw_playwright_context.on("request", handle_request)
                raw_playwright_context.on("requestfailed", handle_request_failed)
                raw_playwright_context.on("response", handle_response)
                raw_playwright_context.on("weberror", handle_web_error)
                raw_playwright_context.on("pageerror", handle_page_error)

                # Set up agent controls for existing pages
                for page in raw_playwright_context.pages:
                    await setup_page_agent_controls(page)

                # Define non-async wrapper function for page event
                def on_page(page):
                    asyncio.create_task(setup_page_agent_controls(page))

                # Set up agent controls for new pages using non-async wrapper
                raw_playwright_context.on("page", on_page)

                send_log(
                    "Log listeners and agent controls attached.",
                    "👂",
                    log_type="status",
                )  # Type: status
            else:
                send_log(
                    "Original _create_context did not return a context.",
                    "⚠️",
                    log_type="status",
                )  # Type: status

            return raw_playwright_context

        BrowserContext._create_context = patched_create_context

        # --- Ensure Tool Call ID ---
        if tool_call_id is None:
            tool_call_id = str(uuid.uuid4())
            send_log(
                f"Generated tool_call_id: {tool_call_id}", "🆔", log_type="status"
            )  # Type: status

        # --- LLM Setup ---
        from .env_utils import get_backend_url

        llm = ChatAnthropic(
            model="claude-3-5-sonnet-20240620",
            base_url=get_backend_url("v1beta/models/claude-3-5-sonnet-20240620"),
            extra_headers={
                "x-operative-api-key": api_key,
                "x-operative-tool-call-id": tool_call_id,
            },
        )
        send_log(
            f"LLM ({llm.model}) configured.", "🤖", log_type="status"
        )  # Type: status

        # --- Agent Callback ---
        async def state_callback(browser_state, agent_output, step_number):
            global agent_instance, screenshot_storage  # Ensure we have access to the agent and screenshot storage

            # Send agent output with type 'agent'
            send_log(f"Step {step_number}", "📍", log_type="agent")
            send_log(f"URL: {browser_state.url}", "🔗", log_type="agent")

            # Capture screenshot at each step
            try:
                if agent_instance and agent_instance.browser_context:
                    # Use the provided helper method to get the current page
                    current_page = (
                        await agent_instance.browser_context.get_current_page()
                    )

                    if current_page:
                        # Take screenshot
                        screenshot_bytes = await current_page.screenshot(
                            type="jpeg", quality=80
                        )
                        screenshot_base64 = base64.b64encode(screenshot_bytes).decode(
                            "utf-8"
                        )

                        # Log screenshot size for debugging
                        send_log(
                            f"Screenshot captured: {len(screenshot_bytes)} bytes, {len(screenshot_base64)} base64 chars",
                            "📊",
                            log_type="status",
                        )

                        # Store screenshot with metadata
                        screenshot_storage.append(
                            {
                                "step": step_number,
                                "url": browser_state.url,
                                "timestamp": asyncio.get_event_loop().time(),
                                "screenshot": screenshot_base64,
                            }
                        )

                        send_log(
                            f"Screenshot stored in storage (total: {len(screenshot_storage)})",
                            "📸",
                            log_type="status",
                        )

                        # Re-inject the overlay
                        send_log(
                            f"Re-injecting overlay after step {step_number} into page {current_page.url}",
                            "🔄",
                            log_type="status",
                        )
                    else:
                        send_log(
                            f"Could not get current page from agent context for step {step_number}",
                            "⚠️",
                            log_type="status",
                        )
                else:
                    send_log(
                        f"Agent instance or browser context not available for step {step_number}",
                        "⚠️",
                        log_type="status",
                    )

            except Exception as e:
                # Add traceback for debugging other potential errors
                import traceback

                tb_str = traceback.format_exc()
                send_log(
                    f"Failed to capture screenshot or re-inject overlay after step: {e}\n{tb_str}",
                    "⚠️",
                    log_type="status",
                )

            # Ensure agent_output is a string before logging
            output_str = str(agent_output)
            send_log(f"Agent Output: {output_str}", "💬", log_type="agent")

        # --- Initialize and Run Agent ---
        agent = Agent(
            task=task,
            llm=llm,
            browser=agent_browser,
            register_new_step_callback=state_callback,
        )
        agent_instance = agent

        send_log(f"Agent starting task: {task}", "🏃", log_type="agent")  # Type: agent
        agent_result = await agent.run()
        send_log("Agent run finished.", "🏁", log_type="agent")  # Type: agent

        # --- Prepare Combined Results ---
        # Convert AgentHistoryList to a serializable format (just stringify)
        serialized_result = str(agent_result)

        # Log information about screenshots before returning
        send_log(
            f"Returning {len(screenshot_storage)} screenshots from run_browser_task",
            "📸",
            log_type="status",
        )
        if screenshot_storage:
            for i, screenshot in enumerate(screenshot_storage):
                send_log(
                    f"Screenshot {i + 1}: Step {screenshot['step']}, {len(screenshot['screenshot'])} base64 chars",
                    "🔢",
                    log_type="status",
                )
        else:
            send_log(
                "No screenshots captured during task execution!", "⚠️", log_type="status"
            )

        # Return the agent result and screenshots
        return {"result": serialized_result, "screenshots": screenshot_storage}

    except Exception as e:
        error_message = f"Error in run_browser_task: {e}\n{traceback.format_exc()}"
        send_log(error_message, "❌", log_type="status")  # Type: status
        return {"result": error_message, "screenshots": screenshot_storage}
    finally:
        # --- Cleanup ---
        # Cancel the screenshot task if it's running
        if screenshot_task:
            screenshot_task.cancel()
            try:
                await screenshot_task
            except asyncio.CancelledError:
                pass
            screenshot_task = None
            send_log("Periodic screenshot task canceled", "🧹", log_type="status")

        # Restore the original bring_to_front method
        if _original_bring_to_front:
            PlaywrightPage.bring_to_front = _original_bring_to_front

        # Ensure patch is restored
        if local_original_create_context:
            BrowserContext._create_context = local_original_create_context
            send_log(
                "Original BrowserContext restored.", "🔧", log_type="status"
            )  # Type: status

        # Close the browser created specifically for this task
        if agent_browser:
            await agent_browser.close()
            agent_browser = None
            send_log(
                "Agent browser resources cleaned up.", "🧹", log_type="status"
            )  # Type: status
        # Close the playwright instance started for this task
        if playwright:
            await playwright.stop()
            playwright = None
            send_log(
                "Playwright instance for task stopped.", "🧹", log_type="status"
            )  # Type: status

        # Clear the global instance if it was set
        agent_instance = None

        # Clear the browser task loop reference
        browser_task_loop = None