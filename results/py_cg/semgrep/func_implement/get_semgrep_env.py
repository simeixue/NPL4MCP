# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/semgrep.py
# module: src.semgrep_mcp.semgrep
# qname: src.semgrep_mcp.semgrep.get_semgrep_env
# lines: 133-145
def get_semgrep_env(top_level_span: trace.Span | None) -> dict[str, str]:
    # Just so we get the debug logs for the MCP server
    env = os.environ.copy()
    env["SEMGREP_LOG_SRCS"] = "mcp"
    if top_level_span and not tracing_disabled:
        env["SEMGREP_TRACE_PARENT_SPAN_ID"] = trace.format_span_id(
            top_level_span.get_span_context().span_id
        )
        env["SEMGREP_TRACE_PARENT_TRACE_ID"] = trace.format_trace_id(
            top_level_span.get_span_context().trace_id
        )

    return env