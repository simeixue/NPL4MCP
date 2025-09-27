# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/git/tests/test_server.py
# module: tests.test_server
# qname: tests.test_server.test_git_add_all_files
# lines: 72-80
def test_git_add_all_files(test_repository):
    file_path = Path(test_repository.working_dir) / "all_file.txt"
    file_path.write_text("adding all")

    result = git_add(test_repository, ["."])

    staged_files = [item.a_path for item in test_repository.index.diff("HEAD")]
    assert "all_file.txt" in staged_files
    assert result == "Files staged successfully"