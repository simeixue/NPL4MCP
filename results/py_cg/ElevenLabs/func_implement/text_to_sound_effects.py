# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/elevenlabs/elevenlabs_mcp/server.py
# module: elevenlabs_mcp.server
# qname: elevenlabs_mcp.server.text_to_sound_effects
# lines: 363-389
def text_to_sound_effects(
    text: str,
    duration_seconds: float = 2.0,
    output_directory: str | None = None,
    output_format: str = "mp3_44100_128",
    loop: bool = False,
) -> TextContent:
    if duration_seconds < 0.5 or duration_seconds > 5:
        make_error("Duration must be between 0.5 and 5 seconds")
    output_path = make_output_path(output_directory, base_path)
    output_file_name = make_output_file("sfx", text, output_path, "mp3")

    audio_data = client.text_to_sound_effects.convert(
        text=text,
        output_format=output_format,
        duration_seconds=duration_seconds,
        loop=loop,
    )
    audio_bytes = b"".join(audio_data)

    with open(output_path / output_file_name, "wb") as f:
        f.write(audio_bytes)

    return TextContent(
        type="text",
        text=f"Success. File saved as: {output_path / output_file_name}",
    )