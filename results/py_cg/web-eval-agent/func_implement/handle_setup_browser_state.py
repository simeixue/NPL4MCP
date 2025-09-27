# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/tool_handlers.py
# module: webEvalAgent.src.tool_handlers
# qname: webEvalAgent.src.tool_handlers.handle_setup_browser_state
# lines: 609-763
async def handle_setup_browser_state(arguments: Dict[str, Any], ctx: Context, api_key: str) -> list[TextContent]:
    """Handle setup_browser_state tool calls
    
    This function launches a non-headless browser for user interaction, allows login/authentication,
    and saves the browser state (cookies, local storage, etc.) to a local file.
    
    Args:
        arguments: The tool arguments, may contain 'url' to navigate to
        ctx: The MCP context for reporting progress
        api_key: The API key for authentication (not used directly here)
        
    Returns:
        list[TextContent]: Confirmation of state saving or error messages
    """
    # Initialize log server
    try:
        start_log_server()
        await asyncio.sleep(1)
        open_log_dashboard()
        send_log("Log dashboard initialized for browser state setup", "🚀")
    except Exception as log_server_error:
        print(f"Warning: Could not start log dashboard: {log_server_error}")
    
    # Get the URL if provided
    url = arguments.get("url", "about:blank")
    
    # Ensure URL has a protocol (add https:// if missing)
    if url != "about:blank" and not url.startswith(("http://", "https://", "file://", "data:", "chrome:", "javascript:")):
        url = "https://" + url
        send_log(f"Added https:// protocol to URL: {url}", "🔗")
    
    # Ensure the state directory exists
    state_dir = os.path.expanduser("~/.operative/browser_state")
    os.makedirs(state_dir, exist_ok=True)
    state_file = os.path.join(state_dir, "state.json")
    
    send_log("🚀 Starting interactive login session", "🚀")
    send_log(f"Browser state will be saved to {state_file}", "💾")
    
    # Create a user data directory if it doesn't exist
    user_data_dir = os.path.expanduser("~/.operative/browser_user_data")
    os.makedirs(user_data_dir, exist_ok=True)
    send_log(f"Using browser user data directory: {user_data_dir}", "📁")
    
    playwright = None
    context = None
    page = None
    
    try:
        # Initialize Playwright
        playwright = await async_playwright().start()
        send_log("Playwright initialized", "🎭")
        
        # Launch browser with a persistent context using the user_data_dir parameter
        # This replaces the previous browser.launch() + context.new_context() approach
        context = await playwright.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,  # Use as a direct parameter instead of an arg
            headless=False,  # Non-headless for user interaction
            args=[
                "--no-sandbox",
                "--disable-blink-features=AutomationControlled"
            ],
            ignore_default_args=["--enable-automation"],
            # Include the context options directly
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 800},
            device_scale_factor=2,
            is_mobile=False,
            has_touch=False,
            locale="en-US",
            timezone_id="America/Los_Angeles",
            permissions=["geolocation", "notifications"]
        )
        
        send_log("Browser launched in interactive mode with persistent context", "🎭")
        
        # Modify the navigator.webdriver property to avoid detection
        await context.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => false,
            });
        """)
        send_log("Browser context created with anti-detection measures", "🛡️")
        
        # Create a new page and navigate to the URL
        page = await context.new_page()
        await page.goto(url)
        send_log(f"🔗 Navigated to: {url}", "🔗")
        
        send_log("Waiting for user interaction (close browser tab or 180s timeout)...", "🖱️")
        
        # Set up an event listener for page close
        page_close_event = asyncio.Event()
        
        # Define the handler function that will be called when page closes
        async def on_page_close():
            send_log("Page close event detected", "👁️")
            page_close_event.set()
        
        # Register the handler to be called when page closes
        page.once("close", lambda: asyncio.create_task(on_page_close()))
        
        # Wait for either the event to be set or timeout
        try:
            # Wait for 180 seconds (3 minutes) or until the page is closed
            await asyncio.wait_for(page_close_event.wait(), timeout=180)
            # If we get here without a timeout exception, the page was closed
            send_log("User closed the browser tab, saving state", "🖱️")
        except asyncio.TimeoutError:
            # If we get a timeout, the 180 seconds elapsed
            send_log("Timeout reached (180s), saving current state", "⚠️")
        
        # Save the browser state to a file
        await context.storage_state(path=state_file)
        
        # Also save cookies for debugging purposes
        cookies = await context.cookies()
        cookies_file = os.path.join(state_dir, "cookies.json")
        with open(cookies_file, 'w') as f:
            json.dump(cookies, f, indent=2)
            
        send_log(f"Saved browser state to {state_file}", "💾")
        send_log(f"Saved cookies to {cookies_file} for reference", "🍪")
        
        return [TextContent(
            type="text",
            text=f"✅ Browser state saved successfully to {state_file}. This state will be used automatically in future web_eval_agent sessions."
        )]
        
    except Exception as e:
        error_msg = f"Error during browser state setup: {e}\n{traceback.format_exc()}"
        send_log(error_msg, "❌")
        return [TextContent(
            type="text",
            text=f"❌ Failed to save browser state: {e}"
        )]
    finally:
        # Close resources in reverse order
        if page:
            try:
                await page.close()
            except Exception:
                pass
        if context:
            try:
                await context.close()
            except Exception:
                pass
        if playwright:
            try:
                await playwright.stop()
            except Exception:
                pass
            
        send_log("Browser session completed", "🏁")