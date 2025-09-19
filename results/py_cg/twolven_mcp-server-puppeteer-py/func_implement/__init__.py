# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/twolven_mcp-server-puppeteer-py/puppeteer.py
# module: puppeteer
# qname: puppeteer.BrowserManager.__init__
# lines: 19-24
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None
        self.console_logs = []
        self.screenshots = {}