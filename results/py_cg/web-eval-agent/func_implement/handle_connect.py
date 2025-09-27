# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/log_server.py
# module: webEvalAgent.src.log_server
# qname: webEvalAgent.src.log_server.handle_connect
# lines: 83-88
def handle_connect():
    # Add client to connected_clients set
    connected_clients.add(request.sid)
    
    # Send status message to dashboard
    send_log(f"Connected to log server at {datetime.now().strftime('%H:%M:%S')}", "✅", log_type='status')