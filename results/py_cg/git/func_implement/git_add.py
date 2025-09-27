# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/git/src/mcp_server_git/server.py
# module: src.mcp_server_git.server
# qname: src.mcp_server_git.server.git_add
# lines: 125-130
def git_add(repo: git.Repo, files: list[str]) -> str:
    if files == ["."]:
        repo.git.add(".")
    else:
        repo.index.add(files)
    return "Files staged successfully"