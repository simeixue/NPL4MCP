# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-nefino/src/mcp_nefino/task_manager.py
# module: src.mcp_nefino.task_manager
# qname: src.mcp_nefino.task_manager.TaskManager.__init__
# lines: 25-27
    def __init__(self):
        """Initialize task manager."""
        self.tasks: Dict[str, Task] = {}