# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils._handle_console_message
# lines: 111-136
async def _handle_console_message(message):
    try:
        text = message.text
        log_entry = {
            "type": message.type,
            "text": text,
            "location": message.location,
            "timestamp": asyncio.get_event_loop().time(),
        }
        console_log_storage.append(log_entry)

        # Check if message has a failure attribute
        if hasattr(message, "failure") and message.failure:
            send_log(
                f"CONSOLE ERROR [{log_entry['type']}]: {log_entry['text']} - {message.failure}",
                "❌",
                log_type="console",
            )
        else:
            send_log(
                f"CONSOLE [{log_entry['type']}]: {log_entry['text']}",
                "🖥️",
                log_type="console",
            )
    except Exception as e:
        send_log(f"Error handling console message: {e}", "❌", log_type="status")