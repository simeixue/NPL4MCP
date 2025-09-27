# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/log_server.py
# module: webEvalAgent.src.log_server
# qname: webEvalAgent.src.log_server.index
# lines: 42-44
def index():
    """Serve the main HTML dashboard page."""
    return render_template('static/index.html')