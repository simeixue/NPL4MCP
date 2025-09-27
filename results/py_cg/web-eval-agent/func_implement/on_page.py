# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils.run_browser_task.patched_create_context.on_page
# lines: 1067-1068
                def on_page(page):
                    asyncio.create_task(setup_page_agent_controls(page))