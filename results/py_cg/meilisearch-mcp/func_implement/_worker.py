# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/logging.py
# module: src.meilisearch_mcp.logging
# qname: src.meilisearch_mcp.logging.AsyncLogHandler._worker
# lines: 22-29
    def _worker(self):
        """Background worker to process logs"""
        while self.running:
            try:
                record = self.buffer.get(timeout=1.0)
                self._write_log(record)
            except:
                continue