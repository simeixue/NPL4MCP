# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/fibery_client.py
# module: src.fibery_mcp_server.fibery_client
# qname: src.fibery_mcp_server.fibery_client.Database.include_database
# lines: 59-65
    def include_database(self) -> bool:
        return not (
            self.name.startswith("fibery/")
            or self.name.startswith("Collaboration~Documents")
            or self.name.endswith("-mixin")
            or self.name == "workflow/workflow"
        )