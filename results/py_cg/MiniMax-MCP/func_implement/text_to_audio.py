# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/MiniMax-MCP/minimax_mcp/server.py
# module: minimax_mcp.server
# qname: minimax_mcp.server.text_to_audio
# lines: 75-144
def text_to_audio(
    text: str,
    output_directory: str = None,
    voice_id: str = DEFAULT_VOICE_ID,
    model: str = DEFAULT_SPEECH_MODEL,
    speed: float = DEFAULT_SPEED,
    vol: float = DEFAULT_VOLUME,
    pitch: int = DEFAULT_PITCH,
    emotion: str = DEFAULT_EMOTION,
    sample_rate: int = DEFAULT_SAMPLE_RATE,
    bitrate: int = DEFAULT_BITRATE,
    channel: int = DEFAULT_CHANNEL,
    format: str = DEFAULT_FORMAT,
    language_boost: str = DEFAULT_LANGUAGE_BOOST,
):
    if not text:
        raise MinimaxRequestError("Text is required.")

    payload = {
        "model": model,
        "text": text,
        "voice_setting": {
            "voice_id": voice_id,
            "speed": speed,
            "vol": vol,
            "pitch": pitch,
            "emotion": emotion
        },
        "audio_setting": {
            "sample_rate": sample_rate,
            "bitrate": bitrate,
            "format": format,
            "channel": channel
        },
        "language_boost": language_boost
    }
    if resource_mode == RESOURCE_MODE_URL:
        payload["output_format"] = "url"
    try:
        response_data = api_client.post("/v1/t2a_v2", json=payload)
        audio_data = response_data.get('data', {}).get('audio', '')
        
        if not audio_data:
            raise MinimaxRequestError(f"Failed to get audio data from response")
        if resource_mode == RESOURCE_MODE_URL:
            return TextContent(
                type="text",
                text=f"Success. Audio URL: {audio_data}"
            )
        # hex->bytes
        audio_bytes = bytes.fromhex(audio_data)

        # save audio to file
        output_path = build_output_path(output_directory, base_path)
        output_file_name = build_output_file("t2a", text, output_path, format)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path / output_file_name, "wb") as f:
            f.write(audio_bytes)

        return TextContent(
            type="text",
            text=f"Success. File saved as: {output_path / output_file_name}. Voice used: {voice_id}",
        )
        
    except MinimaxAPIError as e:
        return TextContent(
            type="text",
            text=f"Failed to generate audio: {str(e)}"
        )