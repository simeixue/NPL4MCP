# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/git/tests/test_server.py
# module: tests.test_server
# qname: tests.test_server.test_git_branch_not_contains
# lines: 60-70
def test_git_branch_not_contains(test_repository):
    # Create a new branch and commit to it
    test_repository.git.checkout("-b", "another-feature-branch")
    Path(test_repository.working_dir / Path("another_feature.txt")).write_text("another feature content")
    test_repository.index.add(["another_feature.txt"])
    commit = test_repository.index.commit("another feature commit")
    test_repository.git.checkout("master")

    result = git_branch(test_repository, "local", not_contains=commit.hexsha)
    assert "another-feature-branch" not in result
    assert "master" in result