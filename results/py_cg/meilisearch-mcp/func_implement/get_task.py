# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/tasks.py
# module: src.meilisearch_mcp.tasks
# qname: src.meilisearch_mcp.tasks.TaskManager.get_task
# lines: 22-28
    def get_task(self, task_uid: int) -> Dict[str, Any]:
        """Get information about a specific task"""
        try:
            task = self.client.get_task(task_uid)
            return serialize_task_results(task)
        except Exception as e:
            raise Exception(f"Failed to get task: {str(e)}")