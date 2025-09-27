# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/git/src/mcp_server_git/server.py
# module: src.mcp_server_git.server
# qname: src.mcp_server_git.server.git_log
# lines: 136-170
def git_log(repo: git.Repo, max_count: int = 10, start_timestamp: Optional[str] = None, end_timestamp: Optional[str] = None) -> list[str]:
    if start_timestamp or end_timestamp:
        # Use git log command with date filtering
        args = []
        if start_timestamp:
            args.extend(['--since', start_timestamp])
        if end_timestamp:
            args.extend(['--until', end_timestamp])
        args.extend(['--format=%H%n%an%n%ad%n%s%n'])
        
        log_output = repo.git.log(*args).split('\n')
        
        log = []
        # Process commits in groups of 4 (hash, author, date, message)
        for i in range(0, len(log_output), 4):
            if i + 3 < len(log_output) and len(log) < max_count:
                log.append(
                    f"Commit: {log_output[i]}\n"
                    f"Author: {log_output[i+1]}\n"
                    f"Date: {log_output[i+2]}\n"
                    f"Message: {log_output[i+3]}\n"
                )
        return log
    else:
        # Use existing logic for simple log without date filtering
        commits = list(repo.iter_commits(max_count=max_count))
        log = []
        for commit in commits:
            log.append(
                f"Commit: {commit.hexsha!r}\n"
                f"Author: {commit.author!r}\n"
                f"Date: {commit.authored_datetime}\n"
                f"Message: {commit.message!r}\n"
            )
        return log