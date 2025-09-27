# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils.handle_request
# lines: 296-297
def handle_request(request):
    asyncio.create_task(_handle_request(request))