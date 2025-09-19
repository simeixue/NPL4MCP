# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/twolven_mcp-server-puppeteer-py/puppeteer.py
# module: puppeteer
# qname: puppeteer.BrowserManager.ensure_browser
# lines: 26-45
    async def ensure_browser(self):
        if not self.browser:
            logger.info("Starting new browser instance...")
            self.playwright = await async_playwright().start()
            self.browser = await self.playwright.chromium.launch(
                headless=False,
                args=['--start-maximized']
            )
            self.page = await self.browser.new_page(
                viewport={"width": 1280, "height": 720}
            )
            
            async def handle_console(msg):
                log_entry = f"[{msg.type}] {msg.text}"
                self.console_logs.append(log_entry)
                logger.info(f"Browser console: {log_entry}")
            
            self.page.on("console", handle_console)
            logger.info("Browser instance started successfully")
        return self.page