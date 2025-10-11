# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/utilities/tracing.py
# module: src.semgrep_mcp.utilities.tracing
# qname: src.semgrep_mcp.utilities.tracing.with_span
# lines: 198-209
def with_span(
    parent_span: trace.Span | None,
    name: str,
) -> Generator[trace.Span | None, None, None]:
    if tracing_disabled or parent_span is None:
        yield None
    else:
        tracer = trace.get_tracer(MCP_SERVICE_NAME)

        context = trace.set_span_in_context(parent_span)
        with tracer.start_as_current_span(name, context=context) as span:
            yield span