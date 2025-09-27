# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils.get_agent_state
# lines: 452-471
def get_agent_state():
    """Get the agent state."""
    global agent_instance
    state = {"paused": False, "stopped": False}

    if agent_instance and hasattr(agent_instance, "state"):
        state = {
            "paused": agent_instance.state.paused,
            "stopped": agent_instance.state.stopped,
        }

    # Send agent state update to frontend
    try:
        from .log_server import socketio

        socketio.emit("agent_state", {"state": state})
    except Exception:
        pass

    return state