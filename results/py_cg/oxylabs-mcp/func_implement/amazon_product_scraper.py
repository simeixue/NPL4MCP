# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/src/oxylabs_mcp/tools/scraper.py
# module: src.oxylabs_mcp.tools.scraper
# qname: src.oxylabs_mcp.tools.scraper.amazon_product_scraper
# lines: 171-219
async def amazon_product_scraper(
    query: url_params.AMAZON_SEARCH_QUERY_PARAM,
    autoselect_variant: url_params.AUTOSELECT_VARIANT_CONTEXT_PARAM = False,  # noqa: FBT002
    currency: url_params.CURRENCY_CONTEXT_PARAM = "",
    parse: url_params.PARSE_PARAM = True,  # noqa: FBT002
    render: url_params.RENDER_PARAM = "",
    user_agent_type: url_params.USER_AGENT_TYPE_PARAM = "",
    domain: url_params.DOMAIN_PARAM = "",
    geo_location: url_params.GEO_LOCATION_PARAM = "",
    locale: url_params.LOCALE_PARAM = "",
    output_format: url_params.OUTPUT_FORMAT_PARAM = "",
) -> str:
    """Scrape Amazon products.

    Supports content parsing, different user agent types, domain,
    geolocation, locale parameters and different output formats.
    Supports Amazon specific parameters such as currency and getting
    more accurate pricing data with auto select variant.
    """
    try:
        async with oxylabs_client() as client:
            payload: dict[str, Any] = {"source": "amazon_product", "query": query}

            context = []
            if autoselect_variant:
                context.append({"key": "autoselect_variant", "value": autoselect_variant})
            if currency:
                context.append({"key": "currency", "value": currency})
            if context:
                payload["context"] = context

            if parse:
                payload["parse"] = parse
            if render:
                payload["render"] = render
            if user_agent_type:
                payload["user_agent_type"] = user_agent_type
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