# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/git/tests/test_server.py
# module: tests.test_server
# qname: tests.test_server.test_git_checkout_existing_branch
# lines: 20-25
def test_git_checkout_existing_branch(test_repository):
    test_repository.git.branch("test-branch")
    result = git_checkout(test_repository, "test-branch")

    assert "Switched to branch 'test-branch'" in result
    assert test_repository.active_branch.name == "test-branch"