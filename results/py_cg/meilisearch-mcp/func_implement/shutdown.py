# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/logging.py
# module: src.meilisearch_mcp.logging
# qname: src.meilisearch_mcp.logging.AsyncLogHandler.shutdown
# lines: 42-45
    def shutdown(self):
        """Shutdown the handler"""
        self.running = False
        self.worker_thread.join()