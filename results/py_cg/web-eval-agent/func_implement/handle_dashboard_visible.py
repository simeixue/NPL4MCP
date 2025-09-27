# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/log_server.py
# module: webEvalAgent.src.log_server
# qname: webEvalAgent.src.log_server.handle_dashboard_visible
# lines: 75-80
def handle_dashboard_visible(data):
    """Mark a dashboard tab as currently visible."""
    tab_id = data.get('tabId')
    if tab_id and tab_id in active_dashboard_tabs:
        # This tab is now the most recently active
        last_tab_activity[tab_id] = datetime.now()