# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/log_server.py
# module: webEvalAgent.src.log_server
# qname: webEvalAgent.src.log_server.handle_disconnect
# lines: 91-111
def handle_disconnect():
    # Remove client from connected_clients set
    if request.sid in connected_clients:
        connected_clients.remove(request.sid)
    
    # Remove any dashboard tabs associated with this session
    tabs_to_remove = []
    for tab_id, tab_sid in active_dashboard_tabs.items():
        if tab_sid == request.sid:
            tabs_to_remove.append(tab_id)
    
    for tab_id in tabs_to_remove:
        active_dashboard_tabs.pop(tab_id, None)
        last_tab_activity.pop(tab_id, None)
    
    # Send status message to dashboard
    # Use try-except as send_log might fail if server isn't fully ready/shutting down
    try:
        send_log(f"Disconnected from log server at {datetime.now().strftime('%H:%M:%S')}", "❌", log_type='status')
    except Exception:
        pass