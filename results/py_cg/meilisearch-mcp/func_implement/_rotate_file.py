# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/logging.py
# module: src.meilisearch_mcp.logging
# qname: src.meilisearch_mcp.logging.FileLogHandler._rotate_file
# lines: 58-61
    def _rotate_file(self):
        """Rotate log file daily"""
        date_str = datetime.now().strftime("%Y-%m-%d")
        self.current_file = self.log_dir / f"meilisearch-mcp-{date_str}.log"