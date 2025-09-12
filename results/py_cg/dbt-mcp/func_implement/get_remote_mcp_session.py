# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/sql/tools.py
# module: src.dbt_mcp.sql.tools
# qname: src.dbt_mcp.sql.tools.SqlToolsManager.get_remote_mcp_session
# lines: 77-93
    async def get_remote_mcp_session(
        self, url: str, headers: dict[str, str]
    ) -> ClientSession:
        streamablehttp_client_context: tuple[
            MemoryObjectReceiveStream[SessionMessage | Exception],
            MemoryObjectSendStream[SessionMessage],
            GetSessionIdCallback,
        ] = await self._stack.enter_async_context(
            streamablehttp_client(
                url=url,
                headers=headers,
            )
        )
        read_stream, write_stream, _ = streamablehttp_client_context
        return await self._stack.enter_async_context(
            ClientSession(read_stream, write_stream)
        )