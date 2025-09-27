# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/src/oxylabs_mcp/tools/ai_studio.py
# module: src.oxylabs_mcp.tools.ai_studio
# qname: src.oxylabs_mcp.tools.ai_studio.ai_scraper
# lines: 103-154
async def ai_scraper(
    url: Annotated[str, Field(description="The URL to scrape")],
    output_format: Annotated[
        Literal["json", "markdown"],
        Field(
            description=(
                "The format of the output. If json, the schema is required. "
                "Markdown returns full text of the page."
            )
        ),
    ] = "markdown",
    schema: Annotated[
        dict[str, Any] | None,
        Field(
            description=(
                "The schema to use for the scrape. Only required if output_format is json."
            )
        ),
    ] = None,
    render_javascript: Annotated[  # noqa: FBT002
        bool,
        Field(
            description=(
                "Whether to render the HTML of the page using javascript. "
                "Much slower, therefore use it only for websites "
                "that require javascript to render the page."
                "Unless user asks to use it, first try to scrape the page without it. "
                "If results are unsatisfactory, try to use it."
            )
        ),
    ] = False,
    geo_location: Annotated[
        str | None, Field(description="Two letter ISO country code to use for the scrape proxy.")
    ] = None,
) -> str:
    """Scrape the contents of the web page and return the data in the specified format.

    Schema is required only if output_format is json.
    'render_javascript' is used to render javascript heavy websites.
    """
    logger.info(
        f"Calling ai_scraper with: {url=}, {output_format=}, {schema=}, {render_javascript=}"
    )
    scraper = AiScraper(api_key=get_and_verify_oxylabs_ai_studio_api_key())
    result = await scraper.scrape_async(
        url=url,
        output_format=output_format,
        schema=schema,
        render_javascript=render_javascript,
        geo_location=geo_location,
    )
    return json.dumps({"data": result.data})