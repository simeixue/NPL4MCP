# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/tasks.py
# module: src.meilisearch_mcp.tasks
# qname: src.meilisearch_mcp.tasks.TaskManager.delete_tasks
# lines: 46-52
    def delete_tasks(self, query_parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Delete tasks based on query parameters"""
        try:
            result = self.client.delete_tasks(query_parameters)
            return serialize_task_results(result)
        except Exception as e:
            raise Exception(f"Failed to delete tasks: {str(e)}")