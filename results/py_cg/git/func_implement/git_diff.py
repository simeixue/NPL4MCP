# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/git/src/mcp_server_git/server.py
# module: src.mcp_server_git.server
# qname: src.mcp_server_git.server.git_diff
# lines: 118-119
def git_diff(repo: git.Repo, target: str, context_lines: int = DEFAULT_CONTEXT_LINES) -> str:
    return repo.git.diff(f"--unified={context_lines}", target)