# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/git/src/mcp_server_git/server.py
# module: src.mcp_server_git.server
# qname: src.mcp_server_git.server.git_commit
# lines: 121-123
def git_commit(repo: git.Repo, message: str) -> str:
    commit = repo.index.commit(message)
    return f"Changes committed successfully with hash {commit.hexsha}"