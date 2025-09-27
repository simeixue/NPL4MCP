# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/elevenlabs/tests/test_utils.py
# module: tests.test_utils
# qname: tests.test_utils.test_make_error
# lines: 16-18
def test_make_error():
    with pytest.raises(ElevenLabsMcpError):
        make_error("Test error")