# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/log_server.py
# module: webEvalAgent.src.log_server
# qname: webEvalAgent.src.log_server.send_browser_view
# lines: 131-154
async def send_browser_view(image_data_url: str):
    """Sends the browser view image data URL to all connected clients."""
    # This function is async because it might be called from the asyncio loop
    # in browser_manager. However, socketio.emit needs to be called carefully
    # when interacting between asyncio and other threads (like Flask's).
    # socketio.emit is generally thread-safe, but ensure the event loop is handled.
    
    # Check if the data URL is valid
    if not image_data_url or not image_data_url.startswith("data:image/"):
        return
    
    # Mark the screencast as running when we receive a browser view update
    try:
        from .browser_utils import set_screencast_running
        set_screencast_running(True)
    except ImportError:
        pass
    except Exception:
        pass
        
    try:
        socketio.emit('browser_update', {'data': image_data_url})
    except Exception:
        pass