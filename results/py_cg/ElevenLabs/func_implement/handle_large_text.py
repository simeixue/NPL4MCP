# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/elevenlabs/elevenlabs_mcp/utils.py
# module: elevenlabs_mcp.utils
# qname: elevenlabs_mcp.utils.handle_large_text
# lines: 139-162
def handle_large_text(
    text: str, max_length: int = 10000, content_type: str = "content"
):
    """
    Handle large text content by saving to temporary file if it exceeds max_length.

    Args:
        text: The text content to handle
        max_length: Maximum character length before saving to temp file
        content_type: Description of the content type for user messages

    Returns:
        str: Either the original text or a message with temp file path
    """
    if len(text) > max_length:
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".txt", delete=False, encoding="utf-8"
        ) as temp_file:
            temp_file.write(text)
            temp_path = temp_file.name

        return f"{content_type.capitalize()} saved to temporary file: {temp_path}\nUse the Read tool to access the full {content_type}."

    return text