# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/MiniMax-MCP/tests/test_utils.py
# module: tests.test_utils
# qname: tests.test_utils.test_try_find_similar_files
# lines: 79-92
def test_try_find_similar_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        test_file = temp_path / "test_file.mp3"
        similar_file = temp_path / "test_file_2.mp3"
        different_file = temp_path / "different.txt"

        test_file.touch()
        similar_file.touch()
        different_file.touch()

        results = try_find_similar_files(str(test_file), temp_path)
        assert len(results) > 0
        assert any(str(similar_file) in str(r) for r in results)