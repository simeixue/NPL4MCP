# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/git/src/mcp_server_git/server.py
# module: src.mcp_server_git.server
# qname: src.mcp_server_git.server.serve.call_tool
# lines: 344-451
    async def call_tool(name: str, arguments: dict) -> list[TextContent]:
        repo_path = Path(arguments["repo_path"])
        
        # For all commands, we need an existing repo
        repo = git.Repo(repo_path)

        match name:
            case GitTools.STATUS:
                status = git_status(repo)
                return [TextContent(
                    type="text",
                    text=f"Repository status:\n{status}"
                )]

            case GitTools.DIFF_UNSTAGED:
                diff = git_diff_unstaged(repo, arguments.get("context_lines", DEFAULT_CONTEXT_LINES))
                return [TextContent(
                    type="text",
                    text=f"Unstaged changes:\n{diff}"
                )]

            case GitTools.DIFF_STAGED:
                diff = git_diff_staged(repo, arguments.get("context_lines", DEFAULT_CONTEXT_LINES))
                return [TextContent(
                    type="text",
                    text=f"Staged changes:\n{diff}"
                )]

            case GitTools.DIFF:
                diff = git_diff(repo, arguments["target"], arguments.get("context_lines", DEFAULT_CONTEXT_LINES))
                return [TextContent(
                    type="text",
                    text=f"Diff with {arguments['target']}:\n{diff}"
                )]

            case GitTools.COMMIT:
                result = git_commit(repo, arguments["message"])
                return [TextContent(
                    type="text",
                    text=result
                )]

            case GitTools.ADD:
                result = git_add(repo, arguments["files"])
                return [TextContent(
                    type="text",
                    text=result
                )]

            case GitTools.RESET:
                result = git_reset(repo)
                return [TextContent(
                    type="text",
                    text=result
                )]

            # Update the LOG case:
            case GitTools.LOG:
                log = git_log(
                    repo, 
                    arguments.get("max_count", 10),
                    arguments.get("start_timestamp"),
                    arguments.get("end_timestamp")
                )
                return [TextContent(
                    type="text",
                    text="Commit history:\n" + "\n".join(log)
                )]
            
            case GitTools.CREATE_BRANCH:
                result = git_create_branch(
                    repo,
                    arguments["branch_name"],
                    arguments.get("base_branch")
                )
                return [TextContent(
                    type="text",
                    text=result
                )]

            case GitTools.CHECKOUT:
                result = git_checkout(repo, arguments["branch_name"])
                return [TextContent(
                    type="text",
                    text=result
                )]

            case GitTools.SHOW:
                result = git_show(repo, arguments["revision"])
                return [TextContent(
                    type="text",
                    text=result
                )]

            case GitTools.BRANCH:
                result = git_branch(
                    repo,
                    arguments.get("branch_type", 'local'),
                    arguments.get("contains", None),
                    arguments.get("not_contains", None),
                )
                return [TextContent(
                    type="text",
                    text=result
                )]
            
            case _:
                raise ValueError(f"Unknown tool: {name}")