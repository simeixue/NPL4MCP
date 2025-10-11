# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/server.py
# module: src.semgrep_mcp.server
# qname: src.semgrep_mcp.server.create_temp_files_from_code_content
# lines: 144-193
def create_temp_files_from_code_content(code_files: list[CodeFile]) -> str:
    """
    Creates temporary files from code content

    Args:
        code_files: List of CodeFile objects

    Returns:
        Path to temporary directory containing the files

    Raises:
        McpError: If there are issues creating or writing to files
    """
    temp_dir = None

    try:
        # Create a temporary directory
        temp_dir = tempfile.mkdtemp(prefix="semgrep_scan_")

        # Create files in the temporary directory
        for file_info in code_files:
            filename = file_info.path
            if not filename:
                continue

            temp_file_path = safe_join(temp_dir, filename)

            try:
                # Create subdirectories if needed
                os.makedirs(os.path.dirname(temp_file_path), exist_ok=True)

                # Write content to file
                with open(temp_file_path, "w") as f:
                    f.write(file_info.content)
            except OSError as e:
                raise McpError(
                    ErrorData(
                        code=INTERNAL_ERROR,
                        message=f"Failed to create or write to file {filename}: {e!s}",
                    )
                ) from e

        return temp_dir
    except Exception as e:
        if temp_dir:
            # Clean up temp directory if creation failed
            shutil.rmtree(temp_dir, ignore_errors=True)
        raise McpError(
            ErrorData(code=INTERNAL_ERROR, message=f"Failed to create temporary files: {e!s}")
        ) from e