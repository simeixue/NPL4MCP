# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils._handle_request
# lines: 139-189
async def _handle_request(request):
    try:
        if not should_log_network_request(request):
            return

        try:
            headers = await request.all_headers()
        except PlaywrightError as e:
            headers = {"error": f"Req Header Error: {e}"}
        except Exception as e:
            headers = {"error": f"Unexpected Req Header Error: {e}"}

        post_data = None
        try:
            if request.post_data:
                post_data_buffer = await request.post_data_buffer()
                if post_data_buffer:
                    try:
                        post_data = post_data_buffer.decode("utf-8", errors="replace")
                    except Exception:
                        post_data = repr(post_data_buffer)
                else:
                    post_data = ""
            else:
                post_data = None
        except PlaywrightError as e:
            post_data = f"Post Data Error: {e}"
        except Exception as e:
            post_data = f"Unexpected Post Data Error: {e}"

        request_entry = {
            "url": request.url,
            "method": request.method,
            "headers": headers,
            "postData": post_data,
            "timestamp": asyncio.get_event_loop().time(),
            "resourceType": request.resource_type,
            "is_navigation": request.is_navigation_request(),
            "id": id(request),
        }
        network_request_storage.append(request_entry)
        send_log(
            f"NET REQ [{request_entry['method']}]: {request_entry['url']}",
            "➡️",
            log_type="network",
        )
    except Exception as e:
        url = request.url if request else "Unknown URL"
        send_log(
            f"Error handling request event for {url}: {e}", "❌", log_type="status"
        )