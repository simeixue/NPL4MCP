# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/log_server.py
# module: webEvalAgent.src.log_server
# qname: webEvalAgent.src.log_server.open_log_dashboard
# lines: 313-335
def open_log_dashboard(url='http://127.0.0.1:5009'):
    """Opens or refreshes the dashboard in the browser."""
    # Try to refresh existing tabs first
    if refresh_dashboard():
        try:
            send_log("Refreshed existing dashboard tab.", "🔄", log_type='status')
        except Exception:
            pass
        return
    
    # No active tabs, open a new one
    try:
        # Use open_new_tab for better control
        webbrowser.open_new_tab(url)
        try:
            send_log(f"Opened new dashboard in browser at {url}.", "🌐", log_type='status')
        except Exception:
            pass
    except Exception as e:
        try:
            send_log(f"Could not open browser automatically: {e}", "⚠️", log_type='status')
        except Exception:
            pass