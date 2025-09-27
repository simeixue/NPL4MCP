# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_manager.py
# module: webEvalAgent.src.browser_manager
# qname: webEvalAgent.src.browser_manager.PlaywrightBrowserManager._handle_response
# lines: 238-263
    async def _handle_response(self, response) -> None:
        """Handle network responses."""
        response_timestamp = asyncio.get_event_loop().time()
        response_data = {
            "status": response.status,
            "statusText": response.status_text,
            "headers": response.headers,
            "timestamp": response_timestamp
        }
        # Find the matching request and update it with response data
        found = False
        for req in self.network_requests:
            # Use id for more reliable matching if available
            if req.get("id") == id(response.request) and "response" not in req:
                req["response"] = response_data
                try:
                    send_log(f"NET RESP [{response_data['status']}]: {req['url']}", "⬅️", log_type='network')
                except Exception:
                    pass
                found = True
                break
        if not found:
             try:
                 send_log(f"NET RESP* [{response_data['status']}]: {response.url} (request not matched)", "⬅️", log_type='network')
             except Exception:
                 pass