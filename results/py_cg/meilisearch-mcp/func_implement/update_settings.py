# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/settings.py
# module: src.meilisearch_mcp.settings
# qname: src.meilisearch_mcp.settings.SettingsManager.update_settings
# lines: 35-43
    def update_settings(
        self, index_uid: str, settings: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Update settings for an index"""
        try:
            index = self.client.index(index_uid)
            return index.update_settings(settings)
        except Exception as e:
            raise Exception(f"Failed to update settings: {str(e)}")