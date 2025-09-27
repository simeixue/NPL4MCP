# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils._handle_request_failed
# lines: 274-288
async def _handle_request_failed(error):
    try:
        error_text = f"REQUEST FAILED: {error}"
        send_log(error_text, "🐛", log_type="console")
        # Add to console_log_storage with type 'error'
        console_log_storage.append(
            {
                "type": "error",
                "text": error_text,
                "location": None,
                "timestamp": asyncio.get_event_loop().time(),
            }
        )
    except Exception as e:
        send_log(f"Error handling request failed: {e}", "❌", log_type="status")