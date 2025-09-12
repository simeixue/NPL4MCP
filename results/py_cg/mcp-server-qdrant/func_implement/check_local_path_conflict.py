# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/src/mcp_server_qdrant/settings.py
# module: src.mcp_server_qdrant.settings
# qname: src.mcp_server_qdrant.settings.QdrantSettings.check_local_path_conflict
# lines: 109-115
    def check_local_path_conflict(self) -> "QdrantSettings":
        if self.local_path:
            if self.location is not None or self.api_key is not None:
                raise ValueError(
                    "If 'local_path' is set, 'location' and 'api_key' must be None."
                )
        return self