# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils.pause_agent
# lines: 410-421
def pause_agent():
    """Pause the agent."""
    global agent_instance
    if agent_instance:
        agent_instance.pause()
        send_log("Agent paused", "⏸️", log_type="status")
        # Send agent state update to frontend
        from .log_server import socketio

        socketio.emit("agent_state", {"state": {"paused": True, "stopped": False}})
        return True
    return False