# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/chat.py
# module: src.meilisearch_mcp.chat
# qname: src.meilisearch_mcp.chat.ChatManager.update_chat_workspace_settings
# lines: 89-106
    async def update_chat_workspace_settings(
        self, workspace_uid: str, settings: Dict[str, Any]
    ) -> Dict[str, Any]:
        try:
            logger.info(f"Updating settings for chat workspace: {workspace_uid}")
            updated_settings = self.client.update_chat_workspace_settings(
                workspace_uid, settings
            )
            logger.info(f"Updated settings for workspace: {workspace_uid}")
            return updated_settings
        except MeilisearchApiError as e:
            logger.error(
                f"Meilisearch API error in update_chat_workspace_settings: {e}"
            )
            raise
        except Exception as e:
            logger.error(f"Error in update_chat_workspace_settings: {e}")
            raise