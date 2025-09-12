# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-nefino/src/mcp_nefino/server.py
# module: src.mcp_nefino.server
# qname: src.mcp_nefino.server.get_news_results
# lines: 129-153
async def get_news_results(
    ctx: Context,
    task_id: str = Field(description="The task ID returned by StartNewsRetrieval"),
) -> str:
    await ctx.session.send_log_message(
        level="info",
        data=f"Checking news retrieval results for task {task_id}",
    )
    try:
        task = ctx.request_context.lifespan_context.task_manager.get_task(task_id)
        if not task:
            return json.dumps({"error": "Task not found"})

        return json.dumps({
            "status": task.status.value,
            "result": task.result,
            "error": task.error
        }, indent=4, ensure_ascii=False)

    except Exception as e:
        await ctx.session.send_log_message(
            level="error",
            data=f"Error getting news results: {str(e)}",
        )
        return f"Failed to get news results: {str(e)}"