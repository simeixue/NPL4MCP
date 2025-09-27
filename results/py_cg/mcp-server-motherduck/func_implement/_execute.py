# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-motherduck/src/mcp_server_motherduck/database.py
# module: src.mcp_server_motherduck.database
# qname: src.mcp_server_motherduck.database.DatabaseClient._execute
# lines: 103-124
    def _execute(self, query: str) -> str:
        if self.conn is None:
            # open short lived readonly connection, run query, close connection, return result
            conn = duckdb.connect(
                self.db_path,
                config={"custom_user_agent": f"mcp-server-motherduck/{SERVER_VERSION}"},
                read_only=self._read_only,
            )
            q = conn.execute(query)
        else:
            q = self.conn.execute(query)

        out = tabulate(
            q.fetchall(),
            headers=[d[0] + "\n" + d[1] for d in q.description],
            tablefmt="pretty",
        )

        if self.conn is None:
            conn.close()

        return out