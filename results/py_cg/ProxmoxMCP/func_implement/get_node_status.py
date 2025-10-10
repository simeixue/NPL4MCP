# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/server.py
# module: src.proxmox_mcp.server
# qname: src.proxmox_mcp.server.ProxmoxMCPServer._setup_tools.get_node_status
# lines: 90-93
        def get_node_status(
            node: Annotated[str, Field(description="Name/ID of node to query (e.g. 'pve1', 'proxmox-node2')")]
        ):
            return self.node_tools.get_node_status(node)