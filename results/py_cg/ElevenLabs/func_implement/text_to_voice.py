# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/elevenlabs/elevenlabs_mcp/server.py
# module: elevenlabs_mcp.server
# qname: elevenlabs_mcp.server.text_to_voice
# lines: 889-922
def text_to_voice(
    voice_description: str,
    text: str | None = None,
    output_directory: str | None = None,
) -> TextContent:
    if voice_description == "":
        make_error("Voice description is required.")

    previews = client.text_to_voice.create_previews(
        voice_description=voice_description,
        text=text,
        auto_generate_text=True if text is None else False,
    )

    output_path = make_output_path(output_directory, base_path)

    generated_voice_ids = []
    output_file_paths = []

    for preview in previews.previews:
        output_file_name = make_output_file(
            "voice_design", preview.generated_voice_id, output_path, "mp3", full_id=True
        )
        output_file_paths.append(str(output_file_name))
        generated_voice_ids.append(preview.generated_voice_id)
        audio_bytes = base64.b64decode(preview.audio_base_64)

        with open(output_path / output_file_name, "wb") as f:
            f.write(audio_bytes)

    return TextContent(
        type="text",
        text=f"Success. Files saved at: {', '.join(output_file_paths)}. Generated voice IDs are: {', '.join(generated_voice_ids)}",
    )