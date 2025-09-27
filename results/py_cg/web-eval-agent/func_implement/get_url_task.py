# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/log_server.py
# module: webEvalAgent.src.log_server
# qname: webEvalAgent.src.log_server.get_url_task
# lines: 53-55
def get_url_task():
    """Return the current URL and task as JSON."""
    return {'url': current_url, 'task': current_task}