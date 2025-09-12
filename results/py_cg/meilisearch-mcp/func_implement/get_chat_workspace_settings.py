# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/chat.py
# module: src.meilisearch_mcp.chat
# qname: src.meilisearch_mcp.chat.ChatManager.get_chat_workspace_settings
# lines: 76-87
    async def get_chat_workspace_settings(self, workspace_uid: str) -> Dict[str, Any]:
        try:
            logger.info(f"Getting settings for chat workspace: {workspace_uid}")
            settings = self.client.get_chat_workspace_settings(workspace_uid)
            logger.info(f"Retrieved settings for workspace: {workspace_uid}")
            return settings
        except MeilisearchApiError as e:
            logger.error(f"Meilisearch API error in get_chat_workspace_settings: {e}")
            raise
        except Exception as e:
            logger.error(f"Error in get_chat_workspace_settings: {e}")
            raise