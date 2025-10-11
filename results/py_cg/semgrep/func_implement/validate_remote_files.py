# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/server.py
# module: src.semgrep_mcp.server
# qname: src.semgrep_mcp.server.validate_remote_files
# lines: 261-285
def validate_remote_files(code_files: list[dict[str, str]]) -> list[CodeFile]:
    """
    Validates the code_files parameter for semgrep scan using Pydantic validation

    Args:
        code_files: List of dictionaries with a "path" and "content" key

    Raises:
        McpError: If validation fails
    """
    if not code_files:
        raise McpError(
            ErrorData(
                code=INVALID_PARAMS, message="code_files must be a non-empty list of file objects"
            )
        )
    try:
        # Pydantic will automatically validate each item in the list
        validated_code_files = [CodeFile.model_validate(file) for file in code_files]

        return validated_code_files
    except Exception as e:
        raise McpError(
            ErrorData(code=INVALID_PARAMS, message=f"Invalid remote code files format: {e!s}")
        ) from e