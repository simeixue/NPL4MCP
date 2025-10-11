# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/fibery-mcp-server/src/fibery_mcp_server/fibery_client.py
# module: src.fibery_mcp_server.fibery_client
# qname: src.fibery_mcp_server.fibery_client.Field.is_workflow
# lines: 27-28
    def is_workflow(self) -> bool:
        return self.__raw_field.get("fibery/name", None) == "workflow/state"