# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils.handle_browser_input
# lines: 482-697
async def handle_browser_input(event_type: str, details: Dict) -> None:
    """Handle browser input events from the frontend.

    Args:
        event_type: The type of input event (click, scroll, keydown, keyup)
        details: The details of the input event

    Returns:
        None
    """
    global active_cdp_session, active_screencast_running

    if event_type != "scroll":
        send_log(
            f"handle_browser_input called with event_type: {event_type}",
            "🔍",
            log_type="status",
        )

    # Check if we have an active CDP session
    if not active_cdp_session:
        send_log("Input error: No active CDP session", "❌", log_type="status")
        return

    # Check if screencast is running
    if not active_screencast_running:
        send_log("Input error: Screencast not running", "❌", log_type="status")
        return

    if event_type != "scroll":
        send_log(f"Processing input: {event_type}", "🔄", log_type="status")

    try:
        if event_type == "click":
            # CDP expects separate press and release events for a click
            button = details.get("button", "left")
            x = details.get("x", 0)
            y = details.get("y", 0)
            click_count = details.get("clickCount", 1)
            # Modifiers might be needed for complex interactions, but start simple
            modifiers = 0  # TODO: Map ctrlKey, shiftKey etc. if needed

            # Mouse Pressed
            mouse_pressed_params = {
                "type": "mousePressed",
                "button": button,
                "x": x,
                "y": y,
                "modifiers": modifiers,
                "clickCount": click_count,
            }

            # send_log(f"Dispatching mousePressed at ({x},{y})", "➡️", log_type='status')
            try:
                await active_cdp_session.send(
                    "Input.dispatchMouseEvent", mouse_pressed_params
                )
                send_log(
                    "mousePressed dispatched successfully", "✅", log_type="status"
                )
            except Exception as press_error:
                send_log(
                    f"Input error: Failed to send mousePressed: {press_error}",
                    "❌",
                    log_type="status",
                )
                return

            # Short delay often helps reliability
            await asyncio.sleep(0.05)

            # Mouse Released
            mouse_released_params = {
                "type": "mouseReleased",
                "button": button,
                "x": x,
                "y": y,
                "modifiers": modifiers,
                "clickCount": click_count,
            }

            # send_log(f"Dispatching mouseReleased at ({x},{y})", "➡️", log_type='status')
            try:
                await active_cdp_session.send(
                    "Input.dispatchMouseEvent", mouse_released_params
                )
                send_log(
                    "mouseReleased dispatched successfully", "✅", log_type="status"
                )
            except Exception as release_error:
                send_log(
                    f"Input error: Failed to send mouseReleased: {release_error}",
                    "❌",
                    log_type="status",
                )
                return

            send_log(f"Click sent at ({x},{y})", "👆", log_type="status")

        elif event_type == "keydown":
            # Map frontend details to CDP key event parameters
            key = details.get("key", "")
            code = details.get("code", "")
            modifiers = _map_modifiers(details)

            # For keyDown events, include the 'text' parameter for printable characters
            # This is necessary for text to appear in input fields
            key_params = {
                "type": "keyDown",
                "modifiers": modifiers,
                "key": key,
                "code": code,
            }

            # Add text parameter for printable characters (letters, numbers, symbols)
            # Skip for special keys like Enter, Escape, Arrow keys, etc.
            if (
                len(key) == 1
            ):  # Simple check for printable characters (single character keys)
                key_params["text"] = key

            # For Backspace, also send the 'deleteBackward' editing command
            if key == "Backspace":
                send_log(
                    "Adding 'deleteBackward' command for Backspace keydown",
                    "🔧",
                    log_type="status",
                )
                key_params["commands"] = ["deleteBackward"]

            try:
                await active_cdp_session.send("Input.dispatchKeyEvent", key_params)
            except Exception as key_error:
                send_log(
                    f"Input error: Failed to send keyDown: {key_error}",
                    "❌",
                    log_type="status",
                )
                return

            send_log(f"Key down sent: {key}", "⌨️", log_type="status")

        elif event_type == "keyup":
            key = details.get("key", "")
            code = details.get("code", "")
            modifiers = _map_modifiers(details)

            key_params = {
                "type": "keyUp",
                "modifiers": modifiers,
                "key": key,
                "code": code,
            }

            try:
                await active_cdp_session.send("Input.dispatchKeyEvent", key_params)
            except Exception as key_error:
                send_log(
                    f"Input error: Failed to send keyUp: {key_error}",
                    "❌",
                    log_type="status",
                )
                return

            send_log(f"Key up sent: {key}", "⌨️", log_type="status")

        elif event_type == "scroll":
            # Use dispatchMouseEvent with type 'mouseWheel'
            x = details.get("x", 0)
            y = details.get("y", 0)
            delta_x = details.get("deltaX", 0)
            delta_y = details.get("deltaY", 0)

            wheel_params = {
                "type": "mouseWheel",
                "x": x,
                "y": y,
                "deltaX": delta_x,
                "deltaY": delta_y,
                "modifiers": 0,  # Modifiers usually not needed for scroll
            }

            try:
                await active_cdp_session.send("Input.dispatchMouseEvent", wheel_params)
            except Exception as wheel_error:
                send_log(
                    f"Input error: Failed to send mouseWheel: {wheel_error}",
                    "❌",
                    log_type="status",
                )
                return

            # send_log(f"Scroll sent: dY={delta_y}", "📜", log_type='status')

        else:
            send_log(f"Unknown input type: {event_type}", "❓", log_type="status")

    except Exception as e:
        send_log(f"Input error: {e}", "❌", log_type="status")

        # Check if the session is closed
        if (
            "Target closed" in str(e)
            or "Session closed" in str(e)
            or "Connection closed" in str(e)
        ):
            send_log(
                "CDP session closed, stopping input handling", "⚠️", log_type="status"
            )
            active_screencast_running = False  # Mark as stopped
            if active_cdp_session:
                try:
                    await active_cdp_session.detach()
                except Exception:
                    pass
                active_cdp_session = None