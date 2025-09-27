# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_manager.py
# module: webEvalAgent.src.browser_manager
# qname: webEvalAgent.src.browser_manager.PlaywrightBrowserManager.get_instance
# lines: 17-21
    def get_instance(cls) -> 'PlaywrightBrowserManager':
        """Get or create the singleton instance of PlaywrightBrowserManager."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance