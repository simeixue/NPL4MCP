# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/git/src/mcp_server_git/server.py
# module: src.mcp_server_git.server
# qname: src.mcp_server_git.server.git_reset
# lines: 132-134
def git_reset(repo: git.Repo) -> str:
    repo.index.reset()
    return "All staged changes reset"