# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/log_server.py
# module: webEvalAgent.src.log_server
# qname: webEvalAgent.src.log_server.set_url_and_task
# lines: 113-117
def set_url_and_task(url: str, task: str):
    """Sets the current URL and task and broadcasts it to all connected clients."""
    global current_url, current_task
    current_url = url
    current_task = task