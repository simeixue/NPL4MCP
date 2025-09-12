# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/MiniMax-MCP/tests/conftest.py
# module: tests.conftest
# qname: tests.conftest.sample_video_file
# lines: 20-23
def sample_video_file(temp_dir):
    video_file = temp_dir / "test.mp4"
    video_file.touch()
    return video_file