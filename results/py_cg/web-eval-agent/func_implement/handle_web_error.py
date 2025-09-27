# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils.handle_web_error
# lines: 308-309
def handle_web_error(error):
    asyncio.create_task(_handle_web_error(error))