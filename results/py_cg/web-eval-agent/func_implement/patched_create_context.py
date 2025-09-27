# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils.run_browser_task.patched_create_context
# lines: 1014-1085
        async def patched_create_context(self, browser_pw):
            if original_create_context is None:
                raise RuntimeError("Original _create_context not stored correctly")

            # Check for persisted browser state
            persisted_state = _get_persisted_state()
            if persisted_state:
                send_log(
                    "Loading persisted browser state in new context",
                    "💾",
                    log_type="status",
                )

            # Call the original method but with storage_state if available
            raw_playwright_context = await original_create_context(self, browser_pw)

            # Apply storage state after context creation if available
            if persisted_state and raw_playwright_context:
                try:
                    with open(persisted_state, "r") as f:
                        state_data = json.load(f)

                    # Load cookies and localStorage from state
                    if "cookies" in state_data:
                        await raw_playwright_context.add_cookies(state_data["cookies"])

                    # Origins with storage set is already handled by Playwright internally
                    send_log(
                        "Applied persisted browser state to context",
                        "💾",
                        log_type="status",
                    )
                except Exception as e:
                    send_log(
                        f"Failed to apply persisted state to context: {e}",
                        "⚠️",
                        log_type="status",
                    )

            if raw_playwright_context:
                # Use the non-async wrapper functions for event listeners
                raw_playwright_context.on("console", handle_console_message)
                raw_playwright_context.on("request", handle_request)
                raw_playwright_context.on("requestfailed", handle_request_failed)
                raw_playwright_context.on("response", handle_response)
                raw_playwright_context.on("weberror", handle_web_error)
                raw_playwright_context.on("pageerror", handle_page_error)

                # Set up agent controls for existing pages
                for page in raw_playwright_context.pages:
                    await setup_page_agent_controls(page)

                # Define non-async wrapper function for page event
                def on_page(page):
                    asyncio.create_task(setup_page_agent_controls(page))

                # Set up agent controls for new pages using non-async wrapper
                raw_playwright_context.on("page", on_page)

                send_log(
                    "Log listeners and agent controls attached.",
                    "👂",
                    log_type="status",
                )  # Type: status
            else:
                send_log(
                    "Original _create_context did not return a context.",
                    "⚠️",
                    log_type="status",
                )  # Type: status

            return raw_playwright_context