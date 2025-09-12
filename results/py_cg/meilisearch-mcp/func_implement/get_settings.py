# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/settings.py
# module: src.meilisearch_mcp.settings
# qname: src.meilisearch_mcp.settings.SettingsManager.get_settings
# lines: 27-33
    def get_settings(self, index_uid: str) -> Dict[str, Any]:
        """Get all settings for an index"""
        try:
            index = self.client.index(index_uid)
            return index.get_settings()
        except Exception as e:
            raise Exception(f"Failed to get settings: {str(e)}")