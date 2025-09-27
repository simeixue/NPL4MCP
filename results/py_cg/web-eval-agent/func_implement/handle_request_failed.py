# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils.handle_request_failed
# lines: 312-313
def handle_request_failed(error):
    asyncio.create_task(_handle_request_failed(error))