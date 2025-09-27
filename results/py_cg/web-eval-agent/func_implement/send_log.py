# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/log_server.py
# module: webEvalAgent.src.log_server
# qname: webEvalAgent.src.log_server.send_log
# lines: 119-128
def send_log(message: str, emoji: str = "➡️", log_type: str = 'agent'):
    """Sends a log message with an emoji prefix and type to all connected clients."""
    # Ensure socketio context is available. If called from a non-SocketIO thread,
    # use socketio.emit directly.
    try:
        log_entry = f"{emoji} {message}"
        # Include log_type in the emitted data
        socketio.emit('log_message', {'data': log_entry, 'type': log_type})
    except Exception:
        pass