# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/log_server.py
# module: webEvalAgent.src.log_server
# qname: webEvalAgent.src.log_server.handle_dashboard_ping
# lines: 68-72
def handle_dashboard_ping(data):
    """Update last activity time for a dashboard tab."""
    tab_id = data.get('tabId')
    if tab_id and tab_id in active_dashboard_tabs:
        last_tab_activity[tab_id] = datetime.now()