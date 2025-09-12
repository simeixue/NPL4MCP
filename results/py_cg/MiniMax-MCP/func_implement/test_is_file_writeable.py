# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/MiniMax-MCP/tests/test_utils.py
# module: tests.test_utils
# qname: tests.test_utils.test_is_file_writeable
# lines: 14-18
def test_is_file_writeable():
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        assert is_file_writeable(temp_path) is True
        assert is_file_writeable(temp_path / "nonexistent.txt") is True