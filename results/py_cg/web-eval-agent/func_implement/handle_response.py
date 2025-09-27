# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils.handle_response
# lines: 300-301
def handle_response(response):
    asyncio.create_task(_handle_response(response))