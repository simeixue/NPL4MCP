# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/MiniMax-MCP/minimax_mcp/server.py
# module: minimax_mcp.server
# qname: minimax_mcp.server.text_to_image
# lines: 514-572
def text_to_image(
    model: str = DEFAULT_T2I_MODEL,
    prompt: str = "",
    aspect_ratio: str = "1:1",
    n: int = 1,
    prompt_optimizer: bool = True,
    output_directory: str = None,
):
    try:
        if not prompt:
            raise MinimaxRequestError("Prompt is required")

        payload = {
            "model": model, 
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "n": n,
            "prompt_optimizer": prompt_optimizer
        }

        response_data = api_client.post("/v1/image_generation", json=payload)
        image_urls = response_data.get("data",{}).get("image_urls",[])
        
        if not image_urls:
            raise MinimaxRequestError("No images generated")
        if resource_mode == RESOURCE_MODE_URL:
            return TextContent(
                type="text",
                text=f"Success. Image URLs: {image_urls}"
            )
        output_path = build_output_path(output_directory, base_path)
        output_file_names = []
        
        for i, image_url in enumerate(image_urls):
            output_file_name = build_output_file("image", f"{i}_{prompt}", output_path, "jpg")
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            image_response = requests.get(image_url)
            image_response.raise_for_status()
            
            with open(output_file_name, 'wb') as f:
                f.write(image_response.content)
            output_file_names.append(output_file_name)
            
        return TextContent(
            type="text",
            text=f"Success. Images saved as: {output_file_names}"
        )
        
    except MinimaxAPIError as e:
        return TextContent(
            type="text",
            text=f"Failed to generate images: {str(e)}"
        )
    except (IOError, requests.RequestException) as e:
        return TextContent(
            type="text",
            text=f"Failed to save images: {str(e)}"
        )