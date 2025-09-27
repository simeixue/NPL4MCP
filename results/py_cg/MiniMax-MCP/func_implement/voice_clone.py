# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/MiniMax-MCP/minimax_mcp/server.py
# module: minimax_mcp.server
# qname: minimax_mcp.server.voice_clone
# lines: 199-271
def voice_clone(
    voice_id: str, 
    file: str,
    text: str,
    output_directory: str = None,
    is_url: bool = False
) -> TextContent:
    try:
        # step1: upload file
        if is_url:
            # download file from url
            response = requests.get(file, stream=True)
            response.raise_for_status()
            files = {'file': ('audio_file.mp3', response.raw, 'audio/mpeg')}
            data = {'purpose': 'voice_clone'}
            response_data = api_client.post("/v1/files/upload", files=files, data=data)
        else:
            # open and upload file
            if not os.path.exists(file):
                raise MinimaxRequestError(f"Local file does not exist: {file}")
            with open(file, 'rb') as f:
                files = {'file': f}
                data = {'purpose': 'voice_clone'}
                response_data = api_client.post("/v1/files/upload", files=files, data=data)
            
        file_id = response_data.get("file",{}).get("file_id")
        if not file_id:
            raise MinimaxRequestError(f"Failed to get file_id from upload response")

        # step2: clone voice
        payload = {
            "file_id": file_id,
            "voice_id": voice_id,
        }
        if text:
            payload["text"] = text
            payload["model"] = DEFAULT_SPEECH_MODEL

        response_data = api_client.post("/v1/voice_clone", json=payload)
        
        if not response_data.get("demo_audio"):
            return TextContent(
                type="text",
                text=f"Voice cloned successfully: Voice ID: {voice_id}"
            )
        if resource_mode == RESOURCE_MODE_URL:
            return TextContent(
                type="text",
                text=f"Success. Demo audio URL: {response_data.get('demo_audio')}"
            )
        # step3: download demo audio
        output_path = build_output_path(output_directory, base_path)
        output_file_name = build_output_file("voice_clone", text, output_path, "wav")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path / output_file_name, "wb") as f:
            f.write(requests.get(response_data.get("demo_audio")).content)

        return TextContent(
            type="text",
            text=f"Voice cloned successfully: Voice ID: {voice_id}, demo audio saved as: {output_path / output_file_name}"
        )
        
    except MinimaxAPIError as e:
        return TextContent(
            type="text",
            text=f"Failed to clone voice: {str(e)}"
        )
    except (IOError, requests.RequestException) as e:
        return TextContent(
            type="text",
            text=f"Failed to handle files: {str(e)}"
        )