# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_manager.py
# module: webEvalAgent.src.browser_manager
# qname: webEvalAgent.src.browser_manager.PlaywrightBrowserManager._handle_screencast_frame
# lines: 266-298
    async def _handle_screencast_frame(self, params: Dict) -> None:
        """Handle incoming screencast frames from CDP."""
        if not self.cdp_session:
            return # Session closed or not initialized

        image_data = params.get('data')
        session_id = params.get('sessionId')

        if image_data and session_id:
            # Format as data URL
            image_data_url = f"data:image/jpeg;base64,{image_data}"

            # Send to frontend via SocketIO
            try:
                # Use asyncio.create_task to avoid blocking the CDP event handler
                asyncio.create_task(send_browser_view(image_data_url))
            except Exception:
                pass

            # IMPORTANT: Acknowledge the frame back to the browser
            try:
                await self.cdp_session.send("Page.screencastFrameAck", {"sessionId": session_id})
            except Exception as e:
                # If acknowledging fails, the stream might stop
                # For now, just handle the error. If the session is closed, this will likely fail.
                if "Target closed" in str(e) or "Session closed" in str(e) or "Connection closed" in str(e):
                    self.screencast_task_running = False # Mark as stopped
                    if self.cdp_session:
                        try:
                            await self.cdp_session.detach()
                        except Exception:
                            pass
                        self.cdp_session = None