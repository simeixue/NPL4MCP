# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils.run_browser_task.state_callback
# lines: 1112-1191
        async def state_callback(browser_state, agent_output, step_number):
            global agent_instance, screenshot_storage  # Ensure we have access to the agent and screenshot storage

            # Send agent output with type 'agent'
            send_log(f"Step {step_number}", "📍", log_type="agent")
            send_log(f"URL: {browser_state.url}", "🔗", log_type="agent")

            # Capture screenshot at each step
            try:
                if agent_instance and agent_instance.browser_context:
                    # Use the provided helper method to get the current page
                    current_page = (
                        await agent_instance.browser_context.get_current_page()
                    )

                    if current_page:
                        # Take screenshot
                        screenshot_bytes = await current_page.screenshot(
                            type="jpeg", quality=80
                        )
                        screenshot_base64 = base64.b64encode(screenshot_bytes).decode(
                            "utf-8"
                        )

                        # Log screenshot size for debugging
                        send_log(
                            f"Screenshot captured: {len(screenshot_bytes)} bytes, {len(screenshot_base64)} base64 chars",
                            "📊",
                            log_type="status",
                        )

                        # Store screenshot with metadata
                        screenshot_storage.append(
                            {
                                "step": step_number,
                                "url": browser_state.url,
                                "timestamp": asyncio.get_event_loop().time(),
                                "screenshot": screenshot_base64,
                            }
                        )

                        send_log(
                            f"Screenshot stored in storage (total: {len(screenshot_storage)})",
                            "📸",
                            log_type="status",
                        )

                        # Re-inject the overlay
                        send_log(
                            f"Re-injecting overlay after step {step_number} into page {current_page.url}",
                            "🔄",
                            log_type="status",
                        )
                    else:
                        send_log(
                            f"Could not get current page from agent context for step {step_number}",
                            "⚠️",
                            log_type="status",
                        )
                else:
                    send_log(
                        f"Agent instance or browser context not available for step {step_number}",
                        "⚠️",
                        log_type="status",
                    )

            except Exception as e:
                # Add traceback for debugging other potential errors
                import traceback

                tb_str = traceback.format_exc()
                send_log(
                    f"Failed to capture screenshot or re-inject overlay after step: {e}\n{tb_str}",
                    "⚠️",
                    log_type="status",
                )

            # Ensure agent_output is a string before logging
            output_str = str(agent_output)
            send_log(f"Agent Output: {output_str}", "💬", log_type="agent")