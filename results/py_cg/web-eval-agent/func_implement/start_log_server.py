# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/log_server.py
# module: webEvalAgent.src.log_server
# qname: webEvalAgent.src.log_server.start_log_server
# lines: 258-289
def start_log_server(host='127.0.0.1', port=5009):
    """Starts the Flask-SocketIO server in a background thread."""
    def run_server():
        # Use eventlet or gevent for production? For local dev, default Flask dev server is fine.
        # Setting log_output=False to reduce console noise from SocketIO itself
        sys.stdout = open(os.devnull, 'w')
        sys.stderr = open(os.devnull, 'w')
        socketio.run(app, host=host, port=port, log_output=False, use_reloader=False, allow_unsafe_werkzeug=True)

    # Check if templates directory exists
    template_dir = os.path.join(os.path.dirname(__file__), '../templates')
    static_dir = os.path.join(template_dir, 'static')
    
    # Create template directory if it doesn't exist
    if not os.path.exists(template_dir):
        os.makedirs(template_dir)
    
    # Create static directory if it doesn't exist
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)
    
    # Create index.html if it's missing
    os.path.join(template_dir, 'index.html')

    # Start the server in a separate thread.
    # run_server uses host/port from the outer scope, so no args needed here.
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()
    
    # Send initial status message
    send_log("Log server thread started.", "🚀", log_type='status')