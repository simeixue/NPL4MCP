# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/web-eval-agent/webEvalAgent/src/browser_utils.py
# module: webEvalAgent.src.browser_utils
# qname: webEvalAgent.src.browser_utils.inject_agent_control_overlay
# lines: 330-370
async def inject_agent_control_overlay(page: PlaywrightPage):
    """Inject the agent control overlay into a page."""
    e1 = None
    e2 = None
    try:
        # First try with evaluate
        try:
            await page.evaluate(AGENT_CONTROL_OVERLAY_JS)
            return True
        except Exception as exc1:
            e1 = exc1
            send_log(
                f"Failed to inject with page.evaluate(): {e1}", "⚠️", log_type="status"
            )
        # Try with add_script_tag as fallback
        try:
            await page.add_script_tag(content=AGENT_CONTROL_OVERLAY_JS)
            return True
        except Exception as exc2:
            e2 = exc2
            send_log(
                f"Failed to inject with page.add_script_tag(): {e2}",
                "⚠️",
                log_type="status",
            )
        # Try with evaluate_handle as last resort
        try:
            await page.evaluate_handle(f"() => {{ {AGENT_CONTROL_OVERLAY_JS} }}")
            return True
        except Exception as e3:
            send_log(
                f"Failed to inject with page.evaluate_handle(): {e3}",
                "⚠️",
                log_type="status",
            )
            raise Exception(f"All injection methods failed: {e1}, {e2}, {e3}")
    except Exception as e:
        send_log(
            f"Failed to inject agent control overlay: {e}", "❌", log_type="status"
        )
        raise