# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/twolven_mcp-server-puppeteer-py/puppeteer.py
# module: puppeteer
# qname: puppeteer.list_tools
# lines: 63-129
async def list_tools():
    return [
        Tool(
            name="puppeteer_navigate",
            description="Navigate to a URL",
            inputSchema={
                "type": "object",
                "properties": {
                    "url": {"type": "string"},
                    "timeout": {"type": "number", "description": "Navigation timeout in milliseconds"}
                },
                "required": ["url"]
            }
        ),
        Tool(
            name="puppeteer_screenshot",
            description="Take a screenshot of the current page or a specific element",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Name for the screenshot"},
                    "selector": {"type": "string", "description": "CSS selector for element to screenshot"},
                    "width": {"type": "number", "description": "Width in pixels (default: 1280)"},
                    "height": {"type": "number", "description": "Height in pixels (default: 720)"},
                    "timeout": {"type": "number", "description": "Timeout in milliseconds for finding elements"}
                },
                "required": ["name"]
            }
        ),
        Tool(
            name="puppeteer_click",
            description="Click an element on the page",
            inputSchema={
                "type": "object",
                "properties": {
                    "selector": {"type": "string", "description": "CSS selector for element to click"},
                    "timeout": {"type": "number", "description": "Timeout in milliseconds"}
                },
                "required": ["selector"]
            }
        ),
        Tool(
            name="puppeteer_fill",
            description="Fill out an input field",
            inputSchema={
                "type": "object",
                "properties": {
                    "selector": {"type": "string", "description": "CSS selector for input field"},
                    "value": {"type": "string", "description": "Value to fill"},
                    "timeout": {"type": "number", "description": "Timeout in milliseconds"}
                },
                "required": ["selector", "value"]
            }
        ),
        Tool(
            name="puppeteer_evaluate",
            description="Execute JavaScript in the browser console",
            inputSchema={
                "type": "object",
                "properties": {
                    "script": {"type": "string", "description": "JavaScript code to execute"},
                    "timeout": {"type": "number", "description": "Timeout in milliseconds"}
                },
                "required": ["script"]
            }
        )
    ]