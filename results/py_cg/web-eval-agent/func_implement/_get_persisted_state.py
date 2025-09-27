# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils._get_persisted_state
# lines: 728-736
def _get_persisted_state() -> Optional[str]:
    """
    Check for and return the path to persisted browser state if it exists.

    Returns:
        Optional[str]: Path to the state file if it exists, None otherwise
    """
    state_file = os.path.expanduser("~/.operative/browser_state/state.json")
    return state_file if os.path.exists(state_file) else None