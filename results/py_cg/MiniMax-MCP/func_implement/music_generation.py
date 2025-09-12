# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/MiniMax-MCP/minimax_mcp/server.py
# module: minimax_mcp.server
# qname: minimax_mcp.server.music_generation
# lines: 597-664
def music_generation(
    prompt: str,
    lyrics: str,
    sample_rate: int = DEFAULT_SAMPLE_RATE,
    bitrate: int = DEFAULT_BITRATE,
    format: str = DEFAULT_FORMAT,
    output_directory: str = None
) -> TextContent:
        try:
            # prompt and lyrics params check
            if not prompt:
                raise MinimaxRequestError("Prompt is required.")
            if not lyrics:
                raise MinimaxRequestError("Lyrics is required.")
            
            # Build request payload
            payload = {
                "model": DEFAULT_MUSIC_MODEL,
                "prompt": prompt,
                "lyrics": lyrics,
                "audio_setting": {
                    "sample_rate": sample_rate,
                    "bitrate": bitrate,
                    "format": format
                },
            }
            if resource_mode == RESOURCE_MODE_URL:
                payload["output_format"] = "url"

            # Call music generation API
            response_data = api_client.post("/v1/music_generation", json=payload)
                    
            # Handle response
            data = response_data.get('data', {})
            audio_hex = data.get('audio', '')

            if resource_mode == RESOURCE_MODE_URL:
                return TextContent(
                    type="text",
                    text=f"Success. Music url: {audio_hex}"
                )

            output_path = build_output_path(output_directory, base_path)
            output_file_name = build_output_file("music", f"{prompt}", output_path, format)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            # hex->bytes
            audio_bytes = bytes.fromhex(audio_hex)

            # save audio to file
            with open(output_path / output_file_name, "wb") as f:
                f.write(audio_bytes)

            return TextContent(
                type="text",
                text=f"Success. Music saved as: {output_path / output_file_name}"
            )
        
        except MinimaxAPIError as e:
            return TextContent(
                type="text",
                text=f"Failed to generate music: {str(e)}"
            )
        except (IOError, requests.RequestException) as e:
            return TextContent(
                type="text",
                text=f"Failed to save music: {str(e)}"
        )