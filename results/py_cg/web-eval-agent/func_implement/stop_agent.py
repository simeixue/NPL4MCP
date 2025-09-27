# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils.stop_agent
# lines: 438-449
def stop_agent():
    """Stop the agent."""
    global agent_instance
    if agent_instance:
        agent_instance.stop()
        send_log("Agent stopped", "⏹️", log_type="status")
        # Send agent state update to frontend
        from .log_server import socketio

        socketio.emit("agent_state", {"state": {"paused": False, "stopped": True}})
        return True
    return False