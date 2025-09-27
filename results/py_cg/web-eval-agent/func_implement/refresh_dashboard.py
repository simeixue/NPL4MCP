# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/log_server.py
# module: webEvalAgent.src.log_server
# qname: webEvalAgent.src.log_server.refresh_dashboard
# lines: 306-311
def refresh_dashboard():
    """Send refresh signal to all connected dashboard tabs."""
    if active_dashboard_tabs:
        socketio.emit('refresh_dashboard', {})
        return True
    return False