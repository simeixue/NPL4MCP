# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/utilities/tracing.py
# module: src.semgrep_mcp.utilities.tracing
# qname: src.semgrep_mcp.utilities.tracing.get_trace_endpoint
# lines: 127-136
def get_trace_endpoint() -> tuple[str, str]:
    """Get the appropriate trace endpoint based on environment."""
    env = os.environ.get("SEMGREP_OTEL_ENDPOINT", "semgrep-dev").lower()

    if env == "semgrep-prod":
        return (DEFAULT_TRACE_ENDPOINT, "semgrep-prod")
    elif env == "semgrep-local":
        return (DEFAULT_LOCAL_ENDPOINT, "semgrep-local")
    else:
        return (DEFAULT_DEV_ENDPOINT, "semgrep-dev")