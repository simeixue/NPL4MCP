# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/logging.py
# module: src.meilisearch_mcp.logging
# qname: src.meilisearch_mcp.logging.MCPLogger._setup_logger
# lines: 80-95
    def _setup_logger(self, log_dir: Optional[str]):
        """Configure logging with multiple handlers"""
        if not self.logger.handlers:
            # Console handler
            console_handler = logging.StreamHandler(sys.stderr)
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

            # File handler for structured logging
            if log_dir:
                self.file_handler = FileLogHandler(log_dir)

            self.logger.setLevel(logging.INFO)