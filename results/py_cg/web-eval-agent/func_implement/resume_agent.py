# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils.resume_agent
# lines: 424-435
def resume_agent():
    """Resume the agent."""
    global agent_instance
    if agent_instance:
        agent_instance.resume()
        send_log("Agent resumed", "▶️", log_type="status")
        # Send agent state update to frontend
        from .log_server import socketio

        socketio.emit("agent_state", {"state": {"paused": False, "stopped": False}})
        return True
    return False