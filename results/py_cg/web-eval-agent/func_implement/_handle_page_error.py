# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils._handle_page_error
# lines: 240-254
async def _handle_page_error(error):
    try:
        error_text = f"PAGE ERROR: {error}"
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
        send_log(f"Error handling page error: {e}", "❌", log_type="status")