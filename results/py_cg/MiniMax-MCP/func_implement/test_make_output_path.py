# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/MiniMax-MCP/tests/test_utils.py
# module: tests.test_utils
# qname: tests.test_utils.test_make_output_path
# lines: 30-59
def test_make_output_path():
    # Test with temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        result = build_output_path(temp_dir)
        assert result == Path(temp_dir)
        assert result.exists()
        assert result.is_dir()

    # Test with None output_directory (should use base_path)
    base_path = "/tmp/test_base"
    result = build_output_path(None, base_path, is_test=True)
    assert result == Path(base_path)
    
    # Test with relative output_directory
    base_path = "/tmp/test_base"
    result = build_output_path("subdir", base_path, is_test=True)
    assert result == Path(base_path) / "subdir"
    
    # Test with absolute output_directory (should ignore base_path)
    abs_path = "/absolute/path"
    result = build_output_path(abs_path, "/some/base/path", is_test=True)
    assert result == Path(abs_path)

    abs_path = "~/absolute/path"
    result = build_output_path(abs_path, "/some/base/path", is_test=True)
    assert result == Path(Path.home() / "absolute/path")
    
    # Test with None base_path (should use desktop)
    result = build_output_path(None, None, is_test=True)
    assert result == Path.home() / "Desktop"