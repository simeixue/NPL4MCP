# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_manager.py
# module: webEvalAgent.src.browser_manager
# qname: webEvalAgent.src.browser_manager.PlaywrightBrowserManager.close
# lines: 75-114
    async def close(self) -> None:
        """Close the browser and Playwright instance."""
        # Stop screencast if running
        if self.cdp_session and self.screencast_task_running:
            try:
                await self.cdp_session.send("Page.stopScreencast")
            except Exception:
                pass
            self.screencast_task_running = False

        # Detach CDP session if exists
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

        if self.browser:
            try:
                await self.browser.close()
            except Exception:
                pass
            self.browser = None
            
        if self.playwright:
            await self.playwright.stop()
            self.playwright = None

        self.is_initialized = False
        self.console_logs = []
        self.network_requests = []
        send_log("Browser manager closed.", "🛑", log_type='status')