# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/git/src/mcp_server_git/server.py
# module: src.mcp_server_git.server
# qname: src.mcp_server_git.server.git_status
# lines: 109-110
def git_status(repo: git.Repo) -> str:
    return repo.git.status()