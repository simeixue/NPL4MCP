# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/MiniMax-MCP/minimax_mcp/server.py
# module: minimax_mcp.server
# qname: minimax_mcp.server.query_video_generation
# lines: 449-495
def query_video_generation(task_id: str, output_directory: str = None) -> TextContent:
    try:
        file_id = None
        response_data = api_client.get(f"/v1/query/video_generation?task_id={task_id}")
        status = response_data.get("status")
        if status == "Fail":
            return TextContent(
                type="text",
                text=f"Video generation FAILED for task_id: {task_id}"
            )
        elif status == "Success":
            file_id = response_data.get("file_id")
            if not file_id:
                raise MinimaxRequestError(f"Missing file_id in success response for task_id: {task_id}")
        else:
            return TextContent(
                type="text",
                text=f"Video generation task is still processing: Task ID: {task_id}"
            )
        file_response = api_client.get(f"/v1/files/retrieve?file_id={file_id}")
        download_url = file_response.get("file", {}).get("download_url")
        if not download_url:
            raise MinimaxRequestError(f"Failed to get download URL for file_id: {file_id}")
        if resource_mode == RESOURCE_MODE_URL:
            return TextContent(
                type="text",
                text=f"Success. Video URL: {download_url}"
            )
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
            text=f"Failed to query video generation status: {str(e)}"
        )