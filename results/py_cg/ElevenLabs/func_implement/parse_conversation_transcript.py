# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/elevenlabs/elevenlabs_mcp/utils.py
# module: elevenlabs_mcp.utils
# qname: elevenlabs_mcp.utils.parse_conversation_transcript
# lines: 165-213
def parse_conversation_transcript(transcript_entries, max_length: int = 50000):
    """
    Parse conversation transcript entries into a formatted string.
    If transcript is too long, save to temporary file and return file path.

    Args:
        transcript_entries: List of transcript entries from conversation response
        max_length: Maximum character length before saving to temp file

    Returns:
        tuple: (transcript_text_or_path, is_temp_file)
    """
    transcript_lines = []
    for entry in transcript_entries:
        speaker = getattr(entry, "role", "Unknown")
        text = getattr(entry, "message", getattr(entry, "text", ""))
        timestamp = getattr(entry, "timestamp", None)

        if timestamp:
            transcript_lines.append(f"[{timestamp}] {speaker}: {text}")
        else:
            transcript_lines.append(f"{speaker}: {text}")

    transcript = (
        "\n".join(transcript_lines) if transcript_lines else "No transcript available"
    )

    # Check if transcript is too long for LLM context window
    if len(transcript) > max_length:
        # Create temporary file
        temp_file = tempfile.SpooledTemporaryFile(
            mode="w+", max_size=0, encoding="utf-8"
        )
        temp_file.write(transcript)
        temp_file.seek(0)

        # Get a persistent temporary file path
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".txt", delete=False, encoding="utf-8"
        ) as persistent_temp:
            persistent_temp.write(transcript)
            temp_path = persistent_temp.name

        return (
            f"Transcript saved to temporary file: {temp_path}\nUse the Read tool to access the full transcript.",
            True,
        )

    return transcript, False