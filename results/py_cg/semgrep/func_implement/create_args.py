# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/semgrep.py
# module: src.semgrep_mcp.semgrep
# qname: src.semgrep_mcp.semgrep.create_args
# lines: 148-155
async def create_args(args: list[str]) -> list[str]:
    semgrep_path = await ensure_semgrep_available()
    _, env_alias = get_trace_endpoint()
    return [
        semgrep_path,
        *args
        + (["--no-trace"] if tracing_disabled else ["--trace", "--trace-endpoint", env_alias]),
    ]