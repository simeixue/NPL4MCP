# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/src/oxylabs_mcp/tools/ai_studio.py
# module: src.oxylabs_mcp.tools.ai_studio
# qname: src.oxylabs_mcp.tools.ai_studio.ai_crawler
# lines: 37-99
async def ai_crawler(
    url: Annotated[str, Field(description="The URL from which crawling will be started.")],
    user_prompt: Annotated[
        str,
        Field(description="What information user wants to extract from the domain."),
    ],
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
            description="The schema to use for the crawl. Only required if output_format is json."
        ),
    ] = None,
    render_javascript: Annotated[  # noqa: FBT002
        bool,
        Field(
            description=(
                "Whether to render the HTML of the page using javascript. Much slower, "
                "therefore use it only for websites "
                "that require javascript to render the page. "
                "Unless user asks to use it, first try to crawl the page without it. "
                "If results are unsatisfactory, try to use it."
            )
        ),
    ] = False,
    return_sources_limit: Annotated[
        int, Field(description="The maximum number of sources to return.", le=50)
    ] = 25,
    geo_location: Annotated[
        str | None, Field(description="Two letter ISO country code to use for the crawl proxy.")
    ] = None,
) -> str:
    """Tool useful for crawling a website from starting url and returning data in a specified format.

    Schema is required only if output_format is json.
    'render_javascript' is used to render javascript heavy websites.
    'return_sources_limit' is used to limit the number of sources to return,
    for example if you expect results from single source, you can set it to 1.
    """  # noqa: E501
    logger.info(
        f"Calling ai_crawler with: {url=}, {user_prompt=}, "
        f"{output_format=}, {schema=}, {render_javascript=}, "
        f"{return_sources_limit=}"
    )
    crawler = AiCrawler(api_key=get_and_verify_oxylabs_ai_studio_api_key())
    result = await crawler.crawl_async(
        url=url,
        user_prompt=user_prompt,
        output_format=output_format,
        schema=schema,
        render_javascript=render_javascript,
        return_sources_limit=return_sources_limit,
        geo_location=geo_location,
    )
    return json.dumps({"data": result.data})