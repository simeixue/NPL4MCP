# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/tasks.py
# module: src.meilisearch_mcp.tasks
# qname: src.meilisearch_mcp.tasks.TaskManager.cancel_tasks
# lines: 38-44
    def cancel_tasks(self, query_parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Cancel tasks based on query parameters"""
        try:
            result = self.client.cancel_tasks(query_parameters)
            return serialize_task_results(result)
        except Exception as e:
            raise Exception(f"Failed to cancel tasks: {str(e)}")