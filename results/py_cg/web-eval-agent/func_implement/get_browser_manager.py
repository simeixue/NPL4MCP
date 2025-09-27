# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/tool_handlers.py
# module: webEvalAgent.src.tool_handlers
# qname: webEvalAgent.src.tool_handlers.get_browser_manager
# lines: 32-41
def get_browser_manager() -> PlaywrightBrowserManager:
    """Get the singleton browser manager instance.
    
    This function provides a centralized way to access the singleton
    PlaywrightBrowserManager instance throughout the application.
    
    Returns:
        PlaywrightBrowserManager: The singleton browser manager instance
    """
    return PlaywrightBrowserManager.get_instance()