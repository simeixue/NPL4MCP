# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/utilities/tracing.py
# module: src.semgrep_mcp.utilities.tracing
# qname: src.semgrep_mcp.utilities.tracing.with_tool_span
# lines: 216-244
def with_tool_span(
    span_name: str | None = None,
) -> Callable[
    [Callable[Concatenate[Context, P], Awaitable[R]]],
    Callable[Concatenate[Context, P], Awaitable[R]],
]:
    """
    Decorator to wrap MCP tools with a tracing span.

    All tools decorated by @with_tool_span must have a Context parameter.

    Args:
        span_name: Optional name for the span. If not provided, uses the function name.
    """

    def decorator(
        func: Callable[Concatenate[Context, P], Awaitable[R]],
    ) -> Callable[Concatenate[Context, P], Awaitable[R]]:
        @functools.wraps(func)
        async def wrapper(ctx: Context, *args: P.args, **kwargs: P.kwargs) -> R:
            context = ctx.request_context.lifespan_context
            name = span_name or func.__name__

            with with_span(context.top_level_span, name):
                return await func(ctx, *args, **kwargs)

        return wrapper

    return decorator