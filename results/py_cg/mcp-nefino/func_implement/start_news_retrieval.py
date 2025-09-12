# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-nefino/src/mcp_nefino/server.py
# module: src.mcp_nefino.server
# qname: src.mcp_nefino.server.start_news_retrieval
# lines: 47-123
async def start_news_retrieval(
    ctx: Context,
    place_id: str = Field(description="The id of the place"),
    place_type: PlaceTypeNews = Field(
        description="The type of the place (PR, CTY, AU, LAU)"
    ),
    range_or_recency: RangeOrRecency | None = Field(
        description="Type of search (RANGE or RECENCY)", default=None
    ),
    last_n_days: int | None = Field(
        description="Number of days to search for (when range_or_recency=RECENCY)",
        default=None,
    ),
    date_range_begin: str | None = Field(
        description="Start date in YYYY-MM-DD format (when range_or_recency=RANGE)",
        default=None,
    ),
    date_range_end: str | None = Field(
        description="End date in YYYY-MM-DD format (when range_or_recency=RANGE)",
        default=None,
    ),
    news_topics: list[NewsTopic] | None = Field(
        description="List of topics to filter by",
        default=None,
    ),
) -> str:
    await ctx.session.send_log_message(
        level="info",
        data="Starting news retrieval task",
    )
    try:
        # Validate inputs based on range_or_recency
        if range_or_recency == RangeOrRecency.RECENCY:
            valid, error = validate_last_n_days(last_n_days)
            if not valid:
                return f"Validation error: {error}"

        elif range_or_recency == RangeOrRecency.RANGE:
            if not validate_date_format(date_range_begin) or not validate_date_format(
                date_range_end
            ):
                return "Validation error: Invalid date format. Use YYYY-MM-DD"

            valid, error = validate_date_range(date_range_begin, date_range_end)
            if not valid:
                return f"Validation error: {error}"

        str_place_type = place_type.value
        str_range_or_recency = range_or_recency.value if range_or_recency else None
        str_news_topics = [topic.value for topic in news_topics] if news_topics else None

        app_ctx = ctx.request_context.lifespan_context
        task_id = app_ctx.task_manager.create_task()

        # Start task execution in background
        asyncio.create_task(
            app_ctx.task_manager.execute_news_task(
                task_id=task_id,
                client=app_ctx.client,
                place_id=place_id,
                place_type=str_place_type,
                range_or_recency=str_range_or_recency,
                last_n_days=last_n_days,
                date_range_begin=date_range_begin,
                date_range_end=date_range_end,
                news_topics=str_news_topics,
            )
        )

        return json.dumps({"task_id": task_id})

    except Exception as e:
        await ctx.session.send_log_message(
            level="error",
            data=f"Error starting news retrieval: {str(e)}",
        )
        return f"Failed to start news retrieval: {str(e)}"