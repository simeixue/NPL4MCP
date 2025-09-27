# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_manager.py
# module: webEvalAgent.src.browser_manager
# qname: webEvalAgent.src.browser_manager.PlaywrightBrowserManager._on_page_error
# lines: 132-133
    def _on_page_error(self, message):
        asyncio.create_task(self._handle_console_message(message))