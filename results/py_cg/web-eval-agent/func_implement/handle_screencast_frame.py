# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils.run_browser_task.handle_screencast_frame
# lines: 861-893
            async def handle_screencast_frame(params):
                if "data" not in params:
                    return

                if "sessionId" not in params:
                    return

                try:
                    # Format as data URL
                    image_data = params["data"]
                    image_data_url = f"data:image/jpeg;base64,{image_data}"

                    # Send to frontend via SocketIO
                    try:
                        from .log_server import send_browser_view
                    except ImportError:
                        return

                    try:
                        await send_browser_view(image_data_url)
                    except Exception:
                        pass

                    # Acknowledge the frame
                    try:
                        await cdp_session.send(
                            "Page.screencastFrameAck",
                            {"sessionId": params["sessionId"]},
                        )
                    except Exception:
                        pass
                except Exception:
                    pass