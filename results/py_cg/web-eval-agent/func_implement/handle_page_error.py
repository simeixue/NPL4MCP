# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils.handle_page_error
# lines: 304-305
def handle_page_error(error):
    asyncio.create_task(_handle_page_error(error))