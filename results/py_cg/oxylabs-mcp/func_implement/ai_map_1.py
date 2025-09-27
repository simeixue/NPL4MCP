# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/src/oxylabs_mcp/tools/ai_studio.py
# module: src.oxylabs_mcp.tools.ai_studio
# qname: src.oxylabs_mcp.tools.ai_studio.ai_map
# lines: 271-310
async def ai_map(
    url: Annotated[str, Field(description="The URL from which URLs mapping will be started.")],
    user_prompt: Annotated[
        str,
        Field(description="What kind of urls user wants to find."),
    ],
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
        str | None, Field(description="Two letter ISO country code to use for the mapping proxy.")
    ] = None,
) -> str:
    """Tool useful for mapping website's urls."""  # noqa: E501
    logger.info(
        f"Calling ai_map with: {url=}, {user_prompt=}, "
        f"{render_javascript=}, "
        f"{return_sources_limit=}"
    )
    ai_map = AiMap(api_key=get_and_verify_oxylabs_ai_studio_api_key())
    result = await ai_map.map_async(
        url=url,
        user_prompt=user_prompt,
        render_javascript=render_javascript,
        return_sources_limit=return_sources_limit,
        geo_location=geo_location,
    )
    return json.dumps({"data": result.data})