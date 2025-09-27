# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils.set_screencast_running
# lines: 714-724
def set_screencast_running(running: bool = True) -> None:
    """Set the active_screencast_running flag.

    Args:
        running: Whether the screencast is running

    Returns:
        None
    """
    global active_screencast_running
    active_screencast_running = running