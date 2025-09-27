# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/git/tests/test_server.py
# module: tests.test_server
# qname: tests.test_server.test_git_checkout_nonexistent_branch
# lines: 27-30
def test_git_checkout_nonexistent_branch(test_repository):

    with pytest.raises(git.GitCommandError):
        git_checkout(test_repository, "nonexistent-branch")