# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/semgrep.py
# module: src.semgrep_mcp.semgrep
# qname: src.semgrep_mcp.semgrep.run_semgrep_process_async
# lines: 158-174
async def run_semgrep_process_async(
    top_level_span: trace.Span | None,
    args: list[str],
) -> asyncio.subprocess.Process:
    env = get_semgrep_env(top_level_span)

    # Execute semgrep command
    process = await asyncio.create_subprocess_exec(
        *await create_args(args),
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        # This ensures that stderr makes it through to
        # the server logs, for debugging purposes.
        stderr=None,
        env=env,
    )
    return process