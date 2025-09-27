# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_manager.py
# module: webEvalAgent.src.browser_manager
# qname: webEvalAgent.src.browser_manager.PlaywrightBrowserManager._map_modifiers
# lines: 446-457
    def _map_modifiers(self, details: Dict) -> int:
        """Maps modifier keys from frontend details to CDP modifier bitmask."""
        modifiers = 0
        if details.get('altKey'):
            modifiers |= 1
        if details.get('ctrlKey'):
            modifiers |= 2
        if details.get('metaKey'):
            modifiers |= 4  # Command key on Mac
        if details.get('shiftKey'):
            modifiers |= 8
        return modifiers