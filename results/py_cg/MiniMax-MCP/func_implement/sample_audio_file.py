# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/MiniMax-MCP/tests/conftest.py
# module: tests.conftest
# qname: tests.conftest.sample_audio_file
# lines: 13-16
def sample_audio_file(temp_dir):
    audio_file = temp_dir / "test.mp3"
    audio_file.touch()
    return audio_file