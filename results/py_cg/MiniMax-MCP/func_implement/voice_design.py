# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/MiniMax-MCP/minimax_mcp/server.py
# module: minimax_mcp.server
# qname: minimax_mcp.server.voice_design
# lines: 680-737
def voice_design(
    prompt: str,
    preview_text: str,
    voice_id: str = None,
    output_directory: str = None,
):
    try:
        if not prompt:
            raise MinimaxRequestError("prompt is required")
        if not preview_text:
            raise MinimaxRequestError("preview_text is required")

       # Build request payload
        payload = {
            "prompt": prompt,
            "preview_text": preview_text
        }
        
        # Add voice_id if provided
        if voice_id:
            payload["voice_id"] = voice_id

        # Call voice design API
        response_data = api_client.post("/v1/voice_design", json=payload)

        # Get the response data
        generated_voice_id = response_data.get('voice_id', '')
        trial_audio_hex = response_data.get('trial_audio', '')
        
        if not generated_voice_id:
            raise MinimaxRequestError("No voice generated")
        if resource_mode == RESOURCE_MODE_URL:
            return TextContent(
                type="text",
                text=f"Success. Voice ID generated: {generated_voice_id}, Trial Audio: {trial_audio_hex}"
            )
        
        # hex->bytes
        audio_bytes = bytes.fromhex(trial_audio_hex)

        # save audio to file
        output_path = build_output_path(output_directory, base_path)
        output_file_name = build_output_file("voice_design", preview_text, output_path, "mp3")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path / output_file_name, "wb") as f:
            f.write(audio_bytes)

        return TextContent(
            type="text",
            text=f"Success. File saved as: {output_path / output_file_name}. Voice ID generated: {generated_voice_id}",
        )
        
    except MinimaxAPIError as e:
        return TextContent(
            type="text",
            text=f"Failed to design voice: {str(e)}"
        )