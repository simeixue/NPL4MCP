# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/server.py
# module: src.semgrep_mcp.server
# qname: src.semgrep_mcp.server.validate_absolute_path
# lines: 109-131
def validate_absolute_path(path_to_validate: str, param_name: str) -> str:
    """Validates an absolute path to ensure it's safe to use"""
    if not Path(path_to_validate).is_absolute():
        raise McpError(
            ErrorData(
                code=INVALID_PARAMS,
                message=f"{param_name} must be an absolute path. Received: {path_to_validate}",
            )
        )

    # Normalize path and ensure no path traversal is possible
    normalized_path = os.path.normpath(path_to_validate)

    # Check if normalized path is still absolute
    if not Path(normalized_path).resolve() == Path(normalized_path):
        raise McpError(
            ErrorData(
                code=INVALID_PARAMS,
                message=f"{param_name} contains invalid path traversal sequences",
            )
        )

    return normalized_path