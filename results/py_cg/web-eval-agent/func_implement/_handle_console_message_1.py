# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_manager.py
# module: webEvalAgent.src.browser_manager
# qname: webEvalAgent.src.browser_manager.PlaywrightBrowserManager._handle_console_message
# lines: 208-220
    async def _handle_console_message(self, message) -> None:
        """Handle console messages from the page."""
        log_entry = {
            "type": message.type,
            "text": message.text,
            "location": message.location,
            "timestamp": asyncio.get_event_loop().time()
        }
        self.console_logs.append(log_entry)
        try:
            send_log(f"CONSOLE [{log_entry['type']}]: {log_entry['text']}", "🖥️", log_type='console')
        except Exception:
            pass