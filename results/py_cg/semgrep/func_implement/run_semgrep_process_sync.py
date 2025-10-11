# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/semgrep.py
# module: src.semgrep_mcp.semgrep
# qname: src.semgrep_mcp.semgrep.run_semgrep_process_sync
# lines: 177-190
async def run_semgrep_process_sync(
    top_level_span: trace.Span | None,
    args: list[str],
) -> subprocess.CompletedProcess[bytes]:
    env = get_semgrep_env(top_level_span)

    # Execute semgrep command
    process = subprocess.run(
        await create_args(args),
        stdin=subprocess.PIPE,
        capture_output=True,
        env=env,
    )
    return process