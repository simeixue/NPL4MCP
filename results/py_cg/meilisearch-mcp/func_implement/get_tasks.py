# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/tasks.py
# module: src.meilisearch_mcp.tasks
# qname: src.meilisearch_mcp.tasks.TaskManager.get_tasks
# lines: 30-36
    def get_tasks(self, parameters: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Get list of tasks with optional filters"""
        try:
            tasks = self.client.get_tasks(parameters)
            return serialize_task_results(tasks)
        except Exception as e:
            raise Exception(f"Failed to get tasks: {str(e)}")