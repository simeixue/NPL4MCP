# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/src/oxylabs_mcp/tools/ai_studio.py
# module: src.oxylabs_mcp.tools.ai_studio
# qname: src.oxylabs_mcp.tools.ai_studio.ai_browser_agent
# lines: 158-202
async def ai_browser_agent(
    url: Annotated[str, Field(description="The URL to start the browser agent navigation from.")],
    task_prompt: Annotated[str, Field(description="What browser agent should do.")],
    output_format: Annotated[
        Literal["json", "markdown", "html", "screenshot"],
        Field(
            description=(
                "The output format. Screenshot is base64 encoded jpeg image. "
                "Markdown returns full text of the page including links. "
                "If json, the schema is required."
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
    geo_location: Annotated[
        str | None, Field(description="Two letter ISO country code to use for the browser proxy.")
    ] = None,
) -> str:
    """Run the browser agent and return the data in the specified format.

    This tool is useful if you need navigate around the website and do some actions.
    It allows navigating to any url, clicking on links, filling forms, scrolling, etc.
    Finally it returns the data in the specified format. Schema is required only if output_format is json.
    'task_prompt' describes what browser agent should achieve
    """  # noqa: E501
    logger.info(
        f"Calling ai_browser_agent with: {url=}, {task_prompt=}, {output_format=}, {schema=}"
    )
    browser_agent = BrowserAgent(api_key=get_and_verify_oxylabs_ai_studio_api_key())
    result = await browser_agent.run_async(
        url=url,
        user_prompt=task_prompt,
        output_format=output_format,
        schema=schema,
        geo_location=geo_location,
    )
    data = result.data.model_dump(mode="json") if result.data else None
    return json.dumps({"data": data})