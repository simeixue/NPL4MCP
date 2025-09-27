# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/log_server.py
# module: webEvalAgent.src.log_server
# qname: webEvalAgent.src.log_server.handle_register_tab
# lines: 59-65
def handle_register_tab(data):
    """Register an active dashboard tab."""
    tab_id = data.get('tabId')
    if tab_id:
        active_dashboard_tabs[tab_id] = request.sid
        last_tab_activity[tab_id] = datetime.now()
        send_log(f"Dashboard tab registered: {tab_id[:8]}...", "📋", log_type='status')