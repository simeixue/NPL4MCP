# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_manager.py
# module: webEvalAgent.src.browser_manager
# qname: webEvalAgent.src.browser_manager.PlaywrightBrowserManager.initialize
# lines: 41-73
    async def initialize(self) -> None:
        """Initialize the Playwright browser if not already initialized."""
        if self.is_initialized:
            return
            
        if not PlaywrightBrowserManager._log_server_started:
            try:
                send_log("Initializing Operative Agent (Browser Manager)...", "🚀", log_type='status')
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    s.connect(('localhost', 5009))
                    s.close()
                    PlaywrightBrowserManager._log_server_started = True
                    send_log("Connected to existing log server (Browser Manager).", "✅", log_type='status')
                except (socket.error, Exception):
                    s.close()
                    start_log_server()
                    await asyncio.sleep(1)
                    # Use the enhanced open_log_dashboard which will refresh existing tabs
                    # instead of opening new ones
                    open_log_dashboard()
                    PlaywrightBrowserManager._log_server_started = True
            except Exception as e:
                send_log(f"Error with log server/dashboard (Browser Manager): {e}", "❌", log_type='status')

        # Import here to avoid module import issues
        from playwright.async_api import async_playwright

        self.playwright = await async_playwright().start()
        # Launch headless
        self.browser = await self.playwright.chromium.launch(headless=True)
        self.is_initialized = True
        send_log("Playwright initialized (Browser Manager - Headless).", "🎭", log_type='status')