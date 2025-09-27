# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils._handle_web_error
# lines: 257-271
async def _handle_web_error(error):
    try:
        error_text = f"JS ERROR: {error.error}: {error.page}"
        send_log(error_text, "🐛", log_type="console")
        # Add to console_log_storage with type 'error'
        console_log_storage.append(
            {
                "type": "error",
                "text": error_text,
                "location": error.page.url if hasattr(error.page, "url") else None,
                "timestamp": asyncio.get_event_loop().time(),
            }
        )
    except Exception as e:
        send_log(f"Error handling web error: {e}", "❌", log_type="status")