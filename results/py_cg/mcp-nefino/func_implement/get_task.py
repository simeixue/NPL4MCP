# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-nefino/src/mcp_nefino/task_manager.py
# module: src.mcp_nefino.task_manager
# qname: src.mcp_nefino.task_manager.TaskManager.get_task
# lines: 39-41
    def get_task(self, task_id: str) -> Task | None:
        """Get task by ID."""
        return self.tasks.get(task_id)