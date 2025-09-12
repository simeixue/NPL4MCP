# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/settings.py
# module: src.meilisearch_mcp.settings
# qname: src.meilisearch_mcp.settings.SettingsManager.reset_settings
# lines: 45-51
    def reset_settings(self, index_uid: str) -> Dict[str, Any]:
        """Reset settings to default values"""
        try:
            index = self.client.index(index_uid)
            return index.reset_settings()
        except Exception as e:
            raise Exception(f"Failed to reset settings: {str(e)}")