# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/log_server.py
# module: webEvalAgent.src.log_server
# qname: webEvalAgent.src.log_server.has_active_dashboard
# lines: 291-304
def has_active_dashboard():
    """Check if there are any active dashboard tabs."""
    # Clean up stale tabs (inactive for more than 30 seconds)
    now = datetime.now()
    stale_tabs = []
    for tab_id, last_activity in last_tab_activity.items():
        if (now - last_activity).total_seconds() > 30:
            stale_tabs.append(tab_id)
    
    for tab_id in stale_tabs:
        active_dashboard_tabs.pop(tab_id, None)
        last_tab_activity.pop(tab_id, None)
    
    return len(active_dashboard_tabs) > 0