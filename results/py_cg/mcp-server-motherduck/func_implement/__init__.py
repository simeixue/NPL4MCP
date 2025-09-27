# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-motherduck/src/mcp_server_motherduck/database.py
# module: src.mcp_server_motherduck.database
# qname: src.mcp_server_motherduck.database.DatabaseClient.__init__
# lines: 14-32
    def __init__(
        self,
        db_path: str | None = None,
        motherduck_token: str | None = None,
        home_dir: str | None = None,
        saas_mode: bool = False,
        read_only: bool = False,
    ):
        self._read_only = read_only
        self.db_path, self.db_type = self._resolve_db_path_type(
            db_path, motherduck_token, saas_mode
        )
        logger.info(f"Database client initialized in `{self.db_type}` mode")

        # Set the home directory for DuckDB
        if home_dir:
            os.environ["HOME"] = home_dir

        self.conn = self._initialize_connection()