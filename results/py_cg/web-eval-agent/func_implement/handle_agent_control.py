# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/log_server.py
# module: webEvalAgent.src.log_server
# qname: webEvalAgent.src.log_server.handle_agent_control
# lines: 158-203
def handle_agent_control(data):
    """Handles agent control events received from the frontend."""
    action = data.get('action')
    
    # Log to the dashboard
    send_log(f"Agent control: {action}", "🤖", log_type='status')
    
    # Import browser_utils to access the agent_instance
    try:
        from .browser_utils import agent_instance
    except ImportError:
        error_msg = "Could not import agent_instance from browser_utils"
        send_log(f"Agent control error: {error_msg}", "❌", log_type='status')
        return
    
    if not agent_instance:
        error_msg = "No active agent instance"
        send_log(f"Agent control error: {error_msg}", "❌", log_type='status')
        return
    
    try:
        if action == 'pause':
            agent_instance.pause()
            send_log("Agent paused", "⏸️", log_type='status')
            # Send updated state
            socketio.emit('agent_state', {'state': {'paused': True, 'stopped': False}})
            
        elif action == 'resume':
            agent_instance.resume()
            send_log("Agent resumed", "▶️", log_type='status')
            # Send updated state
            socketio.emit('agent_state', {'state': {'paused': False, 'stopped': False}})
            
        elif action == 'stop':
            agent_instance.stop()
            send_log("Agent stopped", "⏹️", log_type='status')
            # Send updated state
            socketio.emit('agent_state', {'state': {'paused': False, 'stopped': True}})
            
        else:
            error_msg = f"Unknown agent control action: {action}"
            send_log(f"Agent control error: {error_msg}", "❓", log_type='status')
            
    except Exception as e:
        error_msg = f"Error controlling agent: {e}"
        send_log(f"Agent control error: {error_msg}", "❌", log_type='status')