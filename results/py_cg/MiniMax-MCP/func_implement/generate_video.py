# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/MiniMax-MCP/minimax_mcp/server.py
# module: minimax_mcp.server
# qname: minimax_mcp.server.generate_video
# lines: 320-436
def generate_video(
    model: str = DEFAULT_T2V_MODEL,
    prompt: str = "",
    first_frame_image  = None,
    duration: int = None,
    resolution: str = None,
    output_directory: str = None,
    async_mode: bool = False
):
    try:
        if not prompt:
            raise MinimaxRequestError("Prompt is required")

        # check first_frame_image
        if first_frame_image:
            if not isinstance(first_frame_image, str):
                raise MinimaxRequestError(f"First frame image must be a string, got {type(first_frame_image)}")
            if not first_frame_image.startswith(("http://", "https://", "data:")):
                # if local image, convert to dataurl
                if not os.path.exists(first_frame_image):
                    raise MinimaxRequestError(f"First frame image does not exist: {first_frame_image}")
                with open(first_frame_image, "rb") as f:
                    image_data = f.read()
                    first_frame_image = f"data:image/jpeg;base64,{base64.b64encode(image_data).decode('utf-8')}"

        # step1: submit video generation task
        payload = {
            "model": model,
            "prompt": prompt
        }
        if first_frame_image:
            payload["first_frame_image"] = first_frame_image
        if duration:
            payload["duration"] = duration
        if resolution:
            payload["resolution"] = resolution
        response_data = api_client.post("/v1/video_generation", json=payload)
        task_id = response_data.get("task_id")
        if not task_id:
            raise MinimaxRequestError("Failed to get task_id from response")

        if async_mode:
            return TextContent(
                type="text",
                text=f"Success. Video generation task submitted: Task ID: {task_id}. Please use `query_video_generation` tool to check the status of the task and get the result."
            )

        # step2: wait for video generation task to complete
        file_id = None
        max_retries = 30  # 10 minutes total (30 * 20 seconds)
        retry_interval = 20  # seconds


        # MiniMax-Hailuo-02 model has a longer processing time, so we need to wait for a longer time
        if model == "MiniMax-Hailuo-02":
            max_retries = 60

        for attempt in range(max_retries):
            status_response = api_client.get(f"/v1/query/video_generation?task_id={task_id}")
            status = status_response.get("status")
            
            if status == "Fail":
                raise MinimaxRequestError(f"Video generation failed for task_id: {task_id}")
            elif status == "Success":
                file_id = status_response.get("file_id")
                if file_id:
                    break
                raise MinimaxRequestError(f"Missing file_id in success response for task_id: {task_id}")
            
            # Still processing, wait and retry
            time.sleep(retry_interval)

        if not file_id:
            raise MinimaxRequestError(f"Failed to get file_id for task_id: {task_id}")

        # step3: fetch video result
        file_response = api_client.get(f"/v1/files/retrieve?file_id={file_id}")
        download_url = file_response.get("file", {}).get("download_url")
        
        if not download_url:
            raise MinimaxRequestError(f"Failed to get download URL for file_id: {file_id}")
        if resource_mode == RESOURCE_MODE_URL:
            return TextContent(
                type="text",
                text=f"Success. Video URL: {download_url}"
            )
        # step4: download and save video
        output_path = build_output_path(output_directory, base_path)
        output_file_name = build_output_file("video", task_id, output_path, "mp4", True)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        video_response = requests.get(download_url)
        video_response.raise_for_status()
        
        with open(output_path / output_file_name, "wb") as f:
            f.write(video_response.content)

        return TextContent(
            type="text",
            text=f"Success. Video saved as: {output_path / output_file_name}"
        )

    except MinimaxAPIError as e:
        return TextContent(
            type="text",
            text=f"Failed to generate video: {str(e)}"
        )
    except (IOError, requests.RequestException) as e:
        return TextContent(
            type="text",
            text=f"Failed to handle video file: {str(e)}"
        )
    except Exception as e:
        return TextContent(
            type="text",
            text=f"Unexpected error while generating video: {str(e)}"
        )