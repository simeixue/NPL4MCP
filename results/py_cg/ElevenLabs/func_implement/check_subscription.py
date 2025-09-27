# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/elevenlabs/elevenlabs_mcp/server.py
# module: elevenlabs_mcp.server
# qname: elevenlabs_mcp.server.check_subscription
# lines: 503-505
def check_subscription() -> TextContent:
    subscription = client.user.subscription.get()
    return TextContent(type="text", text=f"{subscription.model_dump_json(indent=2)}")