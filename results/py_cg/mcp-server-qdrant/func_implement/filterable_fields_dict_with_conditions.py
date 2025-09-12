# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/src/mcp_server_qdrant/settings.py
# module: src.mcp_server_qdrant.settings
# qname: src.mcp_server_qdrant.settings.QdrantSettings.filterable_fields_dict_with_conditions
# lines: 99-106
    def filterable_fields_dict_with_conditions(self) -> dict[str, FilterableField]:
        if self.filterable_fields is None:
            return {}
        return {
            field.name: field
            for field in self.filterable_fields
            if field.condition is not None
        }