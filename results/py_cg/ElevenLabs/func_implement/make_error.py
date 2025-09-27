# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/elevenlabs/elevenlabs_mcp/utils.py
# module: elevenlabs_mcp.utils
# qname: elevenlabs_mcp.utils.make_error
# lines: 12-13
def make_error(error_text: str):
    raise ElevenLabsMcpError(error_text)