# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/tool_handlers.py
# module: webEvalAgent.src.tool_handlers
# qname: webEvalAgent.src.tool_handlers.handle_setup_browser_state.on_page_close
# lines: 704-706
        async def on_page_close():
            send_log("Page close event detected", "👁️")
            page_close_event.set()