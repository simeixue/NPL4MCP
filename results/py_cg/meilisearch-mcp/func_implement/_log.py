# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/logging.py
# module: src.meilisearch_mcp.logging
# qname: src.meilisearch_mcp.logging.MCPLogger._log
# lines: 97-111
    def _log(self, level: str, msg: str, **kwargs):
        """Create structured log entry"""
        log_entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": level,
            "message": msg,
            **kwargs,
        }

        # Log to console
        getattr(self.logger, level.lower())(msg)

        # Log structured data to file
        if hasattr(self, "file_handler"):
            self.file_handler.emit(log_entry)