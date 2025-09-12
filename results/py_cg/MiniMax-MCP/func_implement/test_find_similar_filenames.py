# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/MiniMax-MCP/tests/test_utils.py
# module: tests.test_utils
# qname: tests.test_utils.test_find_similar_filenames
# lines: 63-76
def test_find_similar_filenames():
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        test_file = temp_path / "test_file.txt"
        similar_file = temp_path / "test_file_2.txt"
        different_file = temp_path / "different.txt"

        test_file.touch()
        similar_file.touch()
        different_file.touch()

        results = find_similar_filenames(str(test_file), temp_path)
        assert len(results) > 0
        assert any(str(similar_file) in str(r[0]) for r in results)