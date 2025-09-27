# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_manager.py
# module: webEvalAgent.src.browser_manager
# qname: webEvalAgent.src.browser_manager.PlaywrightBrowserManager._on_web_error
# lines: 129-130
    def _on_web_error(self, message):
        asyncio.create_task(self._handle_console_message(message))