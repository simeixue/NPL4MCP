# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/utilities/tracing.py
# module: src.semgrep_mcp.utilities.tracing
# qname: src.semgrep_mcp.utilities.tracing.with_tool_span.decorator
# lines: 231-242
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