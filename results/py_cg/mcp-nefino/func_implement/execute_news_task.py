# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-nefino/src/mcp_nefino/task_manager.py
# module: src.mcp_nefino.task_manager
# qname: src.mcp_nefino.task_manager.TaskManager.execute_news_task
# lines: 43-57
    async def execute_news_task(
        self,
        task_id: str,
        client: NefinoClient,
        **kwargs
    ) -> None:
        """Execute a news retrieval task."""
        task = self.tasks[task_id]
        try:
            result = await client.get_news(**kwargs)
            task.result = result
            task.status = TaskStatus.COMPLETED
        except Exception as e:
            task.error = str(e)
            task.status = TaskStatus.FAILED