# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils.setup_page_agent_controls.handle_frame_navigation
# lines: 386-388
        async def handle_frame_navigation(frame):
            if frame is page.main_frame:
                send_log(f"Page navigated to: {page.url}", "🧭", log_type="status")