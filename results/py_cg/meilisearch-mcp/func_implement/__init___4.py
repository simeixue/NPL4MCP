# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/tasks.py
# module: src.meilisearch_mcp.tasks
# qname: src.meilisearch_mcp.tasks.TaskManager.__init__
# lines: 18-20
    def __init__(self, client: Client):
        """Initialize TaskManager with Meilisearch client"""
        self.client = client