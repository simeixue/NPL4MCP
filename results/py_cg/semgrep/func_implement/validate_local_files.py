# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/server.py
# module: src.semgrep_mcp.server
# qname: src.semgrep_mcp.server.validate_local_files
# lines: 218-258
def validate_local_files(local_files: list[dict[str, str]]) -> list[CodeFile]:
    """
    Validates the local_files parameter for semgrep scan using Pydantic validation

    Args:
        local_files: List of singleton dictionaries with a "path" key

    Raises:
        McpError: If validation fails
    """
    if not local_files:
        raise McpError(
            ErrorData(
                code=INVALID_PARAMS, message="local_files must be a non-empty list of file objects"
            )
        )
    try:
        # Pydantic will automatically validate each item in the list
        validated_local_files = []
        for file in local_files:
            path = file["path"]
            if not Path(path).is_absolute():
                raise McpError(
                    ErrorData(
                        code=INVALID_PARAMS, message="code_files.path must be a absolute path"
                    )
                )
            contents = Path(path).read_text()
            # We need to not use the absolute path here, as there is logic later
            # that raises, to prevent path traversal.
            # In reality, the name of the file is pretty immaterial. We only
            # want the accurate path insofar as we can get the contents (whcih we do here)
            # and so we can remember what original file it corresponds to.
            # Taking the name of the file should be enough.
            validated_local_files.append(CodeFile(path=Path(path).name, content=contents))
    except Exception as e:
        raise McpError(
            ErrorData(code=INVALID_PARAMS, message=f"Invalid local code files format: {e!s}")
        ) from e

    return validated_local_files