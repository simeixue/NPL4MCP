# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/git/tests/test_server.py
# module: tests.test_server
# qname: tests.test_server.test_git_branch_local
# lines: 32-35
def test_git_branch_local(test_repository):
    test_repository.git.branch("new-branch-local")
    result = git_branch(test_repository, "local")
    assert "new-branch-local" in result