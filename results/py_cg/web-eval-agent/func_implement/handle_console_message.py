# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils.handle_console_message
# lines: 292-293
def handle_console_message(message):
    asyncio.create_task(_handle_console_message(message))