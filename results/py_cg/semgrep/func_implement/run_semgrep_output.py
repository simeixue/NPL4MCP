# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/semgrep.py
# module: src.semgrep_mcp.semgrep
# qname: src.semgrep_mcp.semgrep.run_semgrep_output
# lines: 242-264
async def run_semgrep_output(top_level_span: trace.Span | None, args: list[str]) -> str:
    """
    Runs `semgrep` with the given arguments and returns the stdout.
    """
    process = await run_semgrep_process_sync(top_level_span, args)

    if process.stdout is None or process.stderr is None:
        raise McpError(
            ErrorData(
                code=INTERNAL_ERROR,
                message="Error running semgrep: stdout or stderr is None",
            )
        )

    if process.returncode != 0:
        raise McpError(
            ErrorData(
                code=INTERNAL_ERROR,
                message=f"Error running semgrep: ({process.returncode}) {process.stderr.decode()}",
            )
        )

    return process.stdout.decode()