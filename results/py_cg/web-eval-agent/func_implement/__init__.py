# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_manager.py
# module: webEvalAgent.src.browser_manager
# qname: webEvalAgent.src.browser_manager.PlaywrightBrowserManager.__init__
# lines: 23-39
    def __init__(self):
        # Check if an instance already exists
        if PlaywrightBrowserManager._instance is not None:
            send_log("PlaywrightBrowserManager is a singleton. Use get_instance() instead.", "⚠️", log_type='status')
            return
            
        # Set this instance as the singleton
        PlaywrightBrowserManager._instance = self
        
        self.playwright = None
        self.browser = None
        self.page = None
        self.cdp_session = None # Added for CDP
        self.screencast_task_running = False # Added for screencast state
        self.console_logs = []
        self.network_requests = []
        self.is_initialized = False