# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/twolven_mcp-server-puppeteer-py/puppeteer.py
# module: puppeteer
# qname: puppeteer.BrowserManager.check_page_loaded
# lines: 47-57
    async def check_page_loaded(self, page, max_wait=5000):
        """Check if page has loaded successfully within timeout period"""
        try:
            # Wait for any element to appear
            await page.wait_for_selector('body *', timeout=max_wait)
            return True
        except PlaywrightTimeout:
            return False
        except Exception as e:
            logger.error(f"Error checking page load: {e}")
            return False