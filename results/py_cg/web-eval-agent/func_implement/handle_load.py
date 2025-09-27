# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils.setup_page_agent_controls.handle_load
# lines: 398-400
        async def handle_load():
            send_log(f"Page load event on: {page.url}", "🔄", log_type="status")
            await asyncio.sleep(0.5)  # Wait a bit for the page to stabilize