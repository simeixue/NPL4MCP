# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/log_server.py
# module: webEvalAgent.src.log_server
# qname: webEvalAgent.src.log_server.handle_browser_input_event
# lines: 207-255
def handle_browser_input_event(data):
    """Handles browser interaction events received from the frontend."""
    event_type = data.get('type')
    details = data.get('details')
    
    # Log to the dashboard as well
    if event_type != 'scroll':
        send_log(f"Received browser input: {event_type}", "🖱️", log_type='status')
    
    # Import the handle_browser_input function and other utilities from browser_utils
    try:
        from .browser_utils import handle_browser_input, active_cdp_session, get_browser_task_loop
    except ImportError:
        error_msg = "Could not import handle_browser_input from browser_utils"
        send_log(f"Input error: {error_msg}", "❌", log_type='status')
        return
    
    # Check if we have an active CDP session
    if not active_cdp_session:
        error_msg = "No active CDP session for input handling"
        send_log(f"Input error: {error_msg}", "❌", log_type='status')
        return
    
    # Since the browser runs in an asyncio loop, and this handler
    # likely runs in a separate thread (Flask/SocketIO default), we need
    # to schedule the async input handler function in the main loop.
    try:
        # Get the browser task loop from browser_utils
        loop = get_browser_task_loop()
        
        if loop is None:
            send_log("Input error: Browser task loop not available", "❌", log_type='status')
            return
        
        # Schedule the coroutine call
        asyncio.run_coroutine_threadsafe(
            handle_browser_input(event_type, details),
            loop
        )
        if event_type == 'scroll':
            return 
        send_log(f"Input {event_type} scheduled for processing", "✅", log_type='status')
        
    except RuntimeError as e:
        error_msg = f"No running asyncio event loop found: {e}"
        send_log(f"Input error: {error_msg}", "❌", log_type='status')
    except Exception as e:
        error_msg = f"Error scheduling browser input handler: {e}"
        send_log(f"Input error: {error_msg}", "❌", log_type='status')