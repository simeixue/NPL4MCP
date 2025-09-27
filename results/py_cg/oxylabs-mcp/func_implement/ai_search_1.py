# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/src/oxylabs_mcp/tools/ai_studio.py
# module: src.oxylabs_mcp.tools.ai_studio
# qname: src.oxylabs_mcp.tools.ai_studio.ai_search
# lines: 206-246
async def ai_search(
    query: Annotated[str, Field(description="The query to search for.")],
    limit: Annotated[int, Field(description="Maximum number of results to return.", le=50)] = 10,
    render_javascript: Annotated[  # noqa: FBT002
        bool,
        Field(
            description=(
                "Whether to render the HTML of the page using javascript. "
                "Much slower, therefore use it only if user asks to use it."
                "First try to search with setting it to False. "
            )
        ),
    ] = False,
    return_content: Annotated[  # noqa: FBT002
        bool,
        Field(description="Whether to return markdown content of the search results."),
    ] = False,
    geo_location: Annotated[
        str | None, Field(description="Two letter ISO country code to use for the search proxy.")
    ] = None,
) -> str:
    """Search the web based on a provided query.

    'return_content' is used to return markdown content for each search result. If 'return_content'
        is set to True, you don't need to use ai_scraper to get the content of the search results urls,
        because it is already included in the search results.
    if 'return_content' is set to True, prefer lower 'limit' to reduce payload size.
    """  # noqa: E501
    logger.info(
        f"Calling ai_search with: {query=}, {limit=}, {render_javascript=}, {return_content=}"
    )
    search = AiSearch(api_key=get_and_verify_oxylabs_ai_studio_api_key())
    result = await search.search_async(
        query=query,
        limit=limit,
        render_javascript=render_javascript,
        return_content=return_content,
        geo_location=geo_location,
    )
    data = result.model_dump(mode="json")["data"]
    return json.dumps({"data": data})