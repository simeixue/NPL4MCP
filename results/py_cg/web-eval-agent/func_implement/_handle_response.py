# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils._handle_response
# lines: 192-237
async def _handle_response(response):
    req_id = id(response.request)
    url = response.url

    if not should_log_network_request(response.request):
        return

    try:
        try:
            headers = await response.all_headers()
            # Check if content type is JSON
            content_type = headers.get("content-type", "").lower()
            if not ("application/json" in content_type or "+json" in content_type):
                return  # Skip non-JSON responses
        except PlaywrightError as e:
            headers = {"error": f"Resp Header Error: {e}"}
        except Exception as e:
            headers = {"error": f"Unexpected Resp Header Error: {e}"}

        status = response.status

        body_size = -1
        try:
            body_buffer = await response.body()
            body_size = len(body_buffer) if body_buffer else 0
        except Exception:
            pass

        for req in network_request_storage:
            if req.get("id") == req_id and "response_status" not in req:
                req["response_status"] = status
                req["response_headers"] = headers
                req["response_body_size"] = body_size
                req["response_timestamp"] = asyncio.get_event_loop().time()
                send_log(f"NET RESP [{status}]: {url} (JSON)", "⬅️", log_type="network")
                break
        else:
            send_log(
                f"NET RESP* [{status}]: {url} (JSON, req not matched/updated)",
                "⬅️",
                log_type="network",
            )
    except Exception as e:
        send_log(
            f"Error handling response event for {url}: {e}", "❌", log_type="status"
        )