# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/src/oxylabs_mcp/tools/scraper.py
# module: src.oxylabs_mcp.tools.scraper
# qname: src.oxylabs_mcp.tools.scraper.google_search_scraper
# lines: 56-107
async def google_search_scraper(
    query: url_params.GOOGLE_QUERY_PARAM,
    parse: url_params.PARSE_PARAM = True,  # noqa: FBT002
    render: url_params.RENDER_PARAM = "",
    user_agent_type: url_params.USER_AGENT_TYPE_PARAM = "",
    start_page: url_params.START_PAGE_PARAM = 0,
    pages: url_params.PAGES_PARAM = 0,
    limit: url_params.LIMIT_PARAM = 0,
    domain: url_params.DOMAIN_PARAM = "",
    geo_location: url_params.GEO_LOCATION_PARAM = "",
    locale: url_params.LOCALE_PARAM = "",
    ad_mode: url_params.AD_MODE_PARAM = False,  # noqa: FBT002
    output_format: url_params.OUTPUT_FORMAT_PARAM = "",
) -> str:
    """Scrape Google Search results.

    Supports content parsing, different user agent types, pagination,
    domain, geolocation, locale parameters and different output formats.
    """
    try:
        async with oxylabs_client() as client:
            payload: dict[str, Any] = {"query": query}

            if ad_mode:
                payload["source"] = "google_ads"
            else:
                payload["source"] = "google_search"

            if parse:
                payload["parse"] = parse
            if render:
                payload["render"] = render
            if user_agent_type:
                payload["user_agent_type"] = user_agent_type
            if start_page:
                payload["start_page"] = start_page
            if pages:
                payload["pages"] = pages
            if limit:
                payload["limit"] = limit
            if domain:
                payload["domain"] = domain
            if geo_location:
                payload["geo_location"] = geo_location
            if locale:
                payload["locale"] = locale

            response_json = await client.scrape(payload)

            return get_content(response_json, parse=parse, output_format=output_format)
    except MCPServerError as e:
        return await e.process()