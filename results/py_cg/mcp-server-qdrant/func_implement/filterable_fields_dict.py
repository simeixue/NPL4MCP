# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/src/mcp_server_qdrant/settings.py
# module: src.mcp_server_qdrant.settings
# qname: src.mcp_server_qdrant.settings.QdrantSettings.filterable_fields_dict
# lines: 94-97
    def filterable_fields_dict(self) -> dict[str, FilterableField]:
        if self.filterable_fields is None:
            return {}
        return {field.name: field for field in self.filterable_fields}