# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/twolven_mcp-server-puppeteer-py/puppeteer.py
# module: puppeteer
# qname: puppeteer.BrowserManager.ensure_browser.handle_console
# lines: 38-41
            async def handle_console(msg):
                log_entry = f"[{msg.type}] {msg.text}"
                self.console_logs.append(log_entry)
                logger.info(f"Browser console: {log_entry}")