# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/elevenlabs/tests/test_utils.py
# module: tests.test_utils
# qname: tests.test_utils.test_make_output_path
# lines: 37-42
def test_make_output_path():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = make_output_path(temp_dir)
        assert result == Path(temp_dir)
        assert result.exists()
        assert result.is_dir()