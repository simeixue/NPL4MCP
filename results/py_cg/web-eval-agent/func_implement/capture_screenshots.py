# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils.run_browser_task.capture_screenshots
# lines: 942-992
            async def capture_screenshots(page, interval=1 / 30):
                """Capture screenshots at the specified interval in seconds (30 FPS)."""
                global active_screencast_running
                send_log(
                    "Starting periodic screenshot capture at 30 FPS",
                    "🎬",
                    log_type="status",
                )
                try:
                    while active_screencast_running:
                        try:
                            # Take a screenshot
                            screenshot_bytes = await page.screenshot(
                                type="jpeg", quality=80
                            )

                            # Convert to base64
                            screenshot_b64 = base64.b64encode(screenshot_bytes).decode(
                                "utf-8"
                            )

                            # Format as data URL
                            screenshot_data_url = (
                                f"data:image/jpeg;base64,{screenshot_b64}"
                            )

                            # Send to frontend
                            from .log_server import send_browser_view

                            await send_browser_view(screenshot_data_url)

                        except Exception as e:
                            if not active_screencast_running:
                                break
                            # Don't log every error to avoid spamming
                            if (
                                "Target closed" in str(e)
                                or "Session closed" in str(e)
                                or "Connection closed" in str(e)
                            ):
                                active_screencast_running = False
                                break

                        # Wait for the next interval
                        await asyncio.sleep(interval)
                except asyncio.CancelledError:
                    send_log(
                        "Periodic screenshot capture stopped", "🛑", log_type="status"
                    )
                except Exception as e:
                    send_log(f"Screenshot capture error: {e}", "❌", log_type="status")