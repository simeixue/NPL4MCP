# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_manager.py
# module: webEvalAgent.src.browser_manager
# qname: webEvalAgent.src.browser_manager.PlaywrightBrowserManager._handle_request
# lines: 222-236
    async def _handle_request(self, request) -> None:
        """Handle network requests."""
        request_entry = {
            "url": request.url,
            "method": request.method,
            "headers": request.headers,
            "timestamp": asyncio.get_event_loop().time(),
            "resourceType": request.resource_type,
            "id": id(request)
        }
        self.network_requests.append(request_entry)
        try:
            send_log(f"NET REQ [{request_entry['method']}]: {request_entry['url']}", "➡️", log_type='network')
        except Exception:
            pass