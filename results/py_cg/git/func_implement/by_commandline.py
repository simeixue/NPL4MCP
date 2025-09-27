# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/git/src/mcp_server_git/server.py
# module: src.mcp_server_git.server
# qname: src.mcp_server_git.server.serve.list_repos.by_commandline
# lines: 336-337
        def by_commandline() -> Sequence[str]:
            return [str(repository)] if repository is not None else []