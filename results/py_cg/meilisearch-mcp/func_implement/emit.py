# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/logging.py
# module: src.meilisearch_mcp.logging
# qname: src.meilisearch_mcp.logging.AsyncLogHandler.emit
# lines: 35-40
    def emit(self, record: Dict[str, Any]):
        """Add log record to buffer"""
        try:
            self.buffer.put(record, block=False)
        except:
            pass  # Buffer full, skip log