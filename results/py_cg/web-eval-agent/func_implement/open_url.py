# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_manager.py
# module: webEvalAgent.src.browser_manager
# qname: webEvalAgent.src.browser_manager.PlaywrightBrowserManager.open_url
# lines: 135-206
    async def open_url(self, url: str) -> str:
        """Open a URL in the browser and start monitoring console and network.
        The browser will stay open for user interaction."""
        if not self.is_initialized:
            await self.initialize()

        # Stop screencast and close previous page/session if they exist
        if self.cdp_session and self.screencast_task_running:
            try:
                await self.cdp_session.send("Page.stopScreencast")
            except Exception:
                pass
            self.screencast_task_running = False
        if self.cdp_session:
             try:
                 await self.cdp_session.detach()
             except Exception:
                 pass
             self.cdp_session = None
        if self.page:
            try:
                await self.page.close()
            except Exception:
                pass
            self.page = None

        # Clear previous logs and requests
        self.console_logs = []
        self.network_requests = []
        
        # Create a new page
        self.page = await self.browser.new_page()
        
        # Set up console log listener using non-async wrapper functions
        self.page.on("console", self._on_console)
        
        # Set up network request listener using non-async wrapper functions
        self.page.on("request", self._on_request)
        self.page.on("response", self._on_response)
        self.page.on("requestfailed", self._on_request_failed)
        self.page.on("weberror", self._on_web_error)
        self.page.on("pageerror", self._on_page_error)
        # Navigate to the URL
        await self.page.goto(url, wait_until="networkidle")
        send_log(f"Navigated to: {url} (Headless Mode)", "🌍", log_type='agent')

        # --- Start CDP Screencast ---
        try:
            self.cdp_session = await self.page.context.new_cdp_session(self.page)
            # Listen for screencast frames using a non-async wrapper function
            self.cdp_session.on("Page.screencastFrame", self._handle_screencast_frame)
            # Start the screencast
            await self.cdp_session.send("Page.startScreencast", {
                "format": "png",  # jpeg is generally smaller than png
                "quality": 100,     # Adjust quality vs size (0-100)
                "maxWidth": 1920,  # Optional: limit width
                "maxHeight": 1080   # Optional: limit height
            })
            self.screencast_task_running = True
            send_log("CDP screencast started.", "📹", log_type='status')
        except Exception as e:
            send_log(f"Failed to start CDP screencast: {e}", "❌", log_type='status')
            self.screencast_task_running = False
            if self.cdp_session:
                try:
                    await self.cdp_session.detach()
                except Exception:
                    pass
                self.cdp_session = None
            return f"Opened {url}, but failed to start screen streaming."

        return f"Opened {url} successfully in headless mode. Streaming view to dashboard."