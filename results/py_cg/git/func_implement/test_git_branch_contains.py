# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/git/tests/test_server.py
# module: tests.test_server
# qname: tests.test_server.test_git_branch_contains
# lines: 48-58
def test_git_branch_contains(test_repository):
    # Create a new branch and commit to it
    test_repository.git.checkout("-b", "feature-branch")
    Path(test_repository.working_dir / Path("feature.txt")).write_text("feature content")
    test_repository.index.add(["feature.txt"])
    commit = test_repository.index.commit("feature commit")
    test_repository.git.checkout("master")

    result = git_branch(test_repository, "local", contains=commit.hexsha)
    assert "feature-branch" in result
    assert "master" not in result