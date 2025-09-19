# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/twolven_mcp-server-puppeteer-py/puppeteer.py
# module: puppeteer
# qname: puppeteer.call_tool
# lines: 132-244
async def call_tool(name: str, arguments: dict):
    try:
        page = await browser_manager.ensure_browser()
        timeout = arguments.get("timeout", DEFAULT_TIMEOUT)
        
        if name == "puppeteer_navigate":
            url = arguments["url"]
            logger.info(f"Attempting to navigate to {url}")
            nav_timeout = arguments.get("timeout", DEFAULT_NAVIGATION_TIMEOUT)
            
            try:
                await page.goto(url, timeout=nav_timeout)
                # Check if page loaded successfully
                if await browser_manager.check_page_loaded(page):
                    return [TextContent(
                        type="text",
                        text=f"Successfully navigated to {url}"
                    )]
                else:
                    return [TextContent(
                        type="text",
                        text=f"Page load incomplete or failed for {url}. The page might be unavailable or loading too slowly."
                    )]
            except Exception as e:
                return [TextContent(
                    type="text",
                    text=f"Failed to navigate to {url}: {str(e)}"
                )]

        elif name == "puppeteer_screenshot":
            try:
                width = arguments.get("width", 1280)
                height = arguments.get("height", 720)
                await page.set_viewport_size({"width": width, "height": height})
                
                screenshot = None
                if "selector" in arguments:
                    logger.info(f"Taking screenshot of element: {arguments['selector']}")
                    element = await page.wait_for_selector(arguments["selector"], timeout=timeout)
                    if element:
                        screenshot = await element.screenshot()
                else:
                    logger.info("Taking full page screenshot")
                    screenshot = await page.screenshot()
                    
                if screenshot:
                    browser_manager.screenshots[arguments["name"]] = screenshot
                    screenshot_b64 = base64.b64encode(screenshot).decode('utf-8')
                    return [
                        TextContent(
                            type="text",
                            text=f"Screenshot '{arguments['name']}' taken at {width}x{height}"
                        ),
                        ImageContent(
                            type="image",
                            data=screenshot_b64,
                            mimeType="image/png"
                        )
                    ]
            except PlaywrightTimeout:
                return [TextContent(
                    type="text",
                    text=f"Screenshot timeout ({timeout}ms) exceeded"
                )]

        elif name == "puppeteer_click":
            try:
                logger.info(f"Clicking element: {arguments['selector']}")
                await page.click(arguments["selector"], timeout=timeout)
                return [TextContent(
                    type="text",
                    text=f"Clicked: {arguments['selector']}"
                )]
            except PlaywrightTimeout:
                return [TextContent(
                    type="text",
                    text=f"Click timeout ({timeout}ms) exceeded for selector: {arguments['selector']}"
                )]

        elif name == "puppeteer_fill":
            try:
                logger.info(f"Filling element: {arguments['selector']}")
                await page.fill(arguments["selector"], arguments["value"], timeout=timeout)
                return [TextContent(
                    type="text",
                    text=f"Filled {arguments['selector']} with: {arguments['value']}"
                )]
            except PlaywrightTimeout:
                return [TextContent(
                    type="text",
                    text=f"Fill timeout ({timeout}ms) exceeded for selector: {arguments['selector']}"
                )]

        elif name == "puppeteer_evaluate":
            try:
                logger.info("Evaluating JavaScript")
                result = await page.evaluate(arguments["script"])
                return [TextContent(
                    type="text",
                    text=f"Execution result:\n{result}"
                )]
            except Exception as e:
                return [TextContent(
                    type="text",
                    text=f"JavaScript evaluation error: {str(e)}"
                )]

    except Exception as e:
        logger.error(f"Error in {name}: {str(e)}")
        return [TextContent(
            type="text",
            text=f"Error executing {name}: {str(e)}"
        )]