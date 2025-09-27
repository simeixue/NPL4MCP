# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils.setup_page_agent_controls
# lines: 374-406
async def setup_page_agent_controls(page: PlaywrightPage):
    """Set up agent control functions for a page."""
    global agent_instance

    try:
        # Expose agent control functions to the page
        await page.expose_function("pauseAgent", lambda: pause_agent())
        await page.expose_function("resumeAgent", lambda: resume_agent())
        await page.expose_function("stopAgent", lambda: stop_agent())
        await page.expose_function("getAgentState", lambda: get_agent_state())

        # Add navigation listener to re-inject overlay after navigation
        async def handle_frame_navigation(frame):
            if frame is page.main_frame:
                send_log(f"Page navigated to: {page.url}", "🧭", log_type="status")

        # Define async wrapper functions for event listeners
        page.on(
            "framenavigated",
            lambda frame: asyncio.create_task(handle_frame_navigation(frame)),
        )
        send_log("Added navigation listener to page", "🔄", log_type="status")

        # Also listen for load events to re-inject the overlay
        async def handle_load():
            send_log(f"Page load event on: {page.url}", "🔄", log_type="status")
            await asyncio.sleep(0.5)  # Wait a bit for the page to stabilize

        page.on("load", lambda: asyncio.create_task(handle_load()))
        send_log("Added load event listener to page", "🔄", log_type="status")

    except Exception as e:
        send_log(f"Failed to set up agent controls: {e}", "❌", log_type="status")