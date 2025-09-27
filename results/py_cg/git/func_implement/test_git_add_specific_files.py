# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/git/tests/test_server.py
# module: tests.test_server
# qname: tests.test_server.test_git_add_specific_files
# lines: 82-93
def test_git_add_specific_files(test_repository):
    file1 = Path(test_repository.working_dir) / "file1.txt"
    file2 = Path(test_repository.working_dir) / "file2.txt"
    file1.write_text("file 1 content")
    file2.write_text("file 2 content")

    result = git_add(test_repository, ["file1.txt"])

    staged_files = [item.a_path for item in test_repository.index.diff("HEAD")]
    assert "file1.txt" in staged_files
    assert "file2.txt" not in staged_files
    assert result == "Files staged successfully"