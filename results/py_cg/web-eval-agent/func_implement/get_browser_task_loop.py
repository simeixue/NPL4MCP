# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils.get_browser_task_loop
# lines: 475-478
def get_browser_task_loop():
    """Get the asyncio loop used by run_browser_task."""
    global browser_task_loop
    return browser_task_loop