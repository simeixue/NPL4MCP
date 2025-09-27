# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/src/oxylabs_mcp/tools/scraper.py
# module: src.oxylabs_mcp.tools.scraper
# qname: src.oxylabs_mcp.tools.scraper.universal_scraper
# lines: 25-52
async def universal_scraper(
    url: url_params.URL_PARAM,
    render: url_params.RENDER_PARAM = "",
    user_agent_type: url_params.USER_AGENT_TYPE_PARAM = "",
    geo_location: url_params.GEO_LOCATION_PARAM = "",
    output_format: url_params.OUTPUT_FORMAT_PARAM = "",
) -> str:
    """Get a content of any webpage.

    Supports browser rendering, parsing of certain webpages
    and different output formats.
    """
    try:
        async with oxylabs_client() as client:
            payload: dict[str, Any] = {"url": url}

            if render:
                payload["render"] = render
            if user_agent_type:
                payload["user_agent_type"] = user_agent_type
            if geo_location:
                payload["geo_location"] = geo_location

            response_json = await client.scrape(payload)

            return get_content(response_json, output_format=output_format)
    except MCPServerError as e:
        return await e.process()