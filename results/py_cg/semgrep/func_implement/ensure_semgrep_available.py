# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/utilities/utils.py
# module: src.semgrep_mcp.utilities.utils
# qname: src.semgrep_mcp.utilities.utils.ensure_semgrep_available
# lines: 142-178
async def ensure_semgrep_available() -> str:
    """
    Ensures semgrep is available and sets the global path in a thread-safe manner

    Returns:
        Path to semgrep executable

    Raises:
        McpError: If semgrep is not installed or not found
    """
    global SEMGREP_EXECUTABLE

    # Fast path - check if we already have the path
    if SEMGREP_EXECUTABLE:
        return SEMGREP_EXECUTABLE

    # Slow path - acquire lock and find semgrep
    async with _SEMGREP_LOCK:
        # Try to find semgrep
        semgrep_path = find_semgrep_path()

        if not semgrep_path:
            raise McpError(
                ErrorData(
                    code=INTERNAL_ERROR,
                    message="Semgrep is not installed or not in your PATH. "
                    "Please install Semgrep manually before using this tool. "
                    "Installation options: "
                    "pip install semgrep, "
                    "macOS: brew install semgrep, "
                    "Or refer to https://semgrep.dev/docs/getting-started/",
                )
            )

        # Store the path for future use
        SEMGREP_EXECUTABLE = semgrep_path
        return semgrep_path