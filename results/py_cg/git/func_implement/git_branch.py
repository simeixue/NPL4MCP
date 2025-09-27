# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/git/src/mcp_server_git/server.py
# module: src.mcp_server_git.server
# qname: src.mcp_server_git.server.git_branch
# lines: 205-231
def git_branch(repo: git.Repo, branch_type: str, contains: str | None = None, not_contains: str | None = None) -> str:
    match contains:
        case None:
            contains_sha = (None,)
        case _:
            contains_sha = ("--contains", contains)

    match not_contains:
        case None:
            not_contains_sha = (None,)
        case _:
            not_contains_sha = ("--no-contains", not_contains)

    match branch_type:
        case 'local':
            b_type = None
        case 'remote':
            b_type = "-r"
        case 'all':
            b_type = "-a"
        case _:
            return f"Invalid branch type: {branch_type}"

    # None value will be auto deleted by GitPython
    branch_info = repo.git.branch(b_type, *contains_sha, *not_contains_sha)

    return branch_info