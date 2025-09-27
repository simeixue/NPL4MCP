# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/src/oxylabs_mcp/tools/ai_studio.py
# module: src.oxylabs_mcp.tools.ai_studio
# qname: src.oxylabs_mcp.tools.ai_studio.generate_schema
# lines: 250-267
async def generate_schema(
    user_prompt: str,
    app_name: Literal["ai_crawler", "ai_scraper", "browser_agent"],
) -> str:
    """Generate a json schema in openapi format."""
    if app_name == "ai_crawler":
        crawler = AiCrawler(api_key=get_and_verify_oxylabs_ai_studio_api_key())
        schema = crawler.generate_schema(prompt=user_prompt)
    elif app_name == "ai_scraper":
        scraper = AiScraper(api_key=get_and_verify_oxylabs_ai_studio_api_key())
        schema = scraper.generate_schema(prompt=user_prompt)
    elif app_name == "browser_agent":
        browser_agent = BrowserAgent(api_key=get_and_verify_oxylabs_ai_studio_api_key())
        schema = browser_agent.generate_schema(prompt=user_prompt)
    else:
        raise ValueError(f"Invalid app name: {app_name}")

    return json.dumps({"data": schema})