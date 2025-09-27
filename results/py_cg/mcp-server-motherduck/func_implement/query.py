# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-motherduck/src/mcp_server_motherduck/database.py
# module: src.mcp_server_motherduck.database
# qname: src.mcp_server_motherduck.database.DatabaseClient.query
# lines: 126-131
    def query(self, query: str) -> str:
        try:
            return self._execute(query)

        except Exception as e:
            raise ValueError(f"❌ Error executing query: {e}")