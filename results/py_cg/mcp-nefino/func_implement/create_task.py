# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-nefino/src/mcp_nefino/task_manager.py
# module: src.mcp_nefino.task_manager
# qname: src.mcp_nefino.task_manager.TaskManager.create_task
# lines: 29-37
    def create_task(self) -> str:
        """Create a new task and return its ID."""
        task_id = str(uuid.uuid4())
        self.tasks[task_id] = Task(
            id=task_id,
            status=TaskStatus.PENDING,
            created_at=datetime.now()
        )
        return task_id