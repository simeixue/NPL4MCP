# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_manager.py
# module: webEvalAgent.src.browser_manager
# qname: webEvalAgent.src.browser_manager.PlaywrightBrowserManager._on_request_failed
# lines: 126-127
    def _on_request_failed(self, message):
        asyncio.create_task(self._handle_console_message(message))