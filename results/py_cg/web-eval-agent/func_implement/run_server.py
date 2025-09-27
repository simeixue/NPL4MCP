# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/log_server.py
# module: webEvalAgent.src.log_server
# qname: webEvalAgent.src.log_server.start_log_server.run_server
# lines: 260-265
    def run_server():
        # Use eventlet or gevent for production? For local dev, default Flask dev server is fine.
        # Setting log_output=False to reduce console noise from SocketIO itself
        sys.stdout = open(os.devnull, 'w')
        sys.stderr = open(os.devnull, 'w')
        socketio.run(app, host=host, port=port, log_output=False, use_reloader=False, allow_unsafe_werkzeug=True)