# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/logging.py
# module: src.meilisearch_mcp.logging
# qname: src.meilisearch_mcp.logging.FileLogHandler._write_log
# lines: 63-70
    def _write_log(self, record: Dict[str, Any]):
        """Write log record to file"""
        current_date = datetime.now().strftime("%Y-%m-%d")
        if not self.current_file or current_date not in self.current_file.name:
            self._rotate_file()

        with open(self.current_file, "a") as f:
            f.write(json.dumps(record) + "\n")