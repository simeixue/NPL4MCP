# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/elevenlabs/elevenlabs_mcp/server.py
# module: elevenlabs_mcp.server
# qname: elevenlabs_mcp.server.speech_to_text
# lines: 281-325
def speech_to_text(
    input_file_path: str,
    language_code: str | None = None,
    diarize: bool = False,
    save_transcript_to_file: bool = True,
    return_transcript_to_client_directly: bool = False,
    output_directory: str | None = None,
) -> TextContent:
    if not save_transcript_to_file and not return_transcript_to_client_directly:
        make_error("Must save transcript to file or return it to the client directly.")
    file_path = handle_input_file(input_file_path)
    if save_transcript_to_file:
        output_path = make_output_path(output_directory, base_path)
        output_file_name = make_output_file("stt", file_path.name, output_path, "txt")
    with file_path.open("rb") as f:
        audio_bytes = f.read()

    if language_code == "" or language_code is None:
        language_code = None

    transcription = client.speech_to_text.convert(
        model_id="scribe_v1",
        file=audio_bytes,
        language_code=language_code,
        enable_logging=True,
        diarize=diarize,
        tag_audio_events=True,
    )

    # Format transcript with speaker identification if diarization was enabled
    if diarize:
        formatted_transcript = format_diarized_transcript(transcription)
    else:
        formatted_transcript = transcription.text

    if save_transcript_to_file:
        with open(output_path / output_file_name, "w") as f:
            f.write(formatted_transcript)

    if return_transcript_to_client_directly:
        return TextContent(type="text", text=formatted_transcript)
    else:
        return TextContent(
            type="text", text=f"Transcription saved to {output_path / output_file_name}"
        )