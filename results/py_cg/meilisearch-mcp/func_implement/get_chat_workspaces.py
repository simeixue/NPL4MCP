# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/chat.py
# module: src.meilisearch_mcp.chat
# qname: src.meilisearch_mcp.chat.ChatManager.get_chat_workspaces
# lines: 59-74
    async def get_chat_workspaces(
        self, offset: Optional[int] = None, limit: Optional[int] = None
    ) -> Dict[str, Any]:
        try:
            logger.info(f"Getting chat workspaces (offset={offset}, limit={limit})")
            workspaces = self.client.get_chat_workspaces(offset=offset, limit=limit)
            logger.info(
                f"Retrieved {len(workspaces.get('results', []))} chat workspaces"
            )
            return workspaces
        except MeilisearchApiError as e:
            logger.error(f"Meilisearch API error in get_chat_workspaces: {e}")
            raise
        except Exception as e:
            logger.error(f"Error in get_chat_workspaces: {e}")
            raise