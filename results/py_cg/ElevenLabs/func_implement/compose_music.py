# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/elevenlabs/elevenlabs_mcp/server.py
# module: elevenlabs_mcp.server
# qname: elevenlabs_mcp.server.compose_music
# lines: 1121-1156
def compose_music(
    prompt: str | None = None,
    output_directory: str | None = None,
    composition_plan: MusicPrompt | None = None,
    music_length_ms: int | None = None,
) -> TextContent:
    if prompt is None and composition_plan is None:
        make_error(
            f"Either prompt or composition_plan must be provided. Prompt: {prompt}"
        )

    if prompt is not None and composition_plan is not None:
        make_error("Only one of prompt or composition_plan must be provided")

    if music_length_ms is not None and composition_plan is not None:
        make_error("music_length_ms cannot be used if composition_plan is provided")

    output_path = make_output_path(output_directory, base_path)
    output_file_name = make_output_file("music", "", output_path, "mp3")

    audio_data = client.music.compose(
        prompt=prompt,
        music_length_ms=music_length_ms,
        composition_plan=composition_plan,
    )

    audio_bytes = b"".join(audio_data)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path / output_file_name, "wb") as f:
        f.write(audio_bytes)

    return TextContent(
        type="text",
        text=f"Success. File saved as: {output_path / output_file_name}.",
    )