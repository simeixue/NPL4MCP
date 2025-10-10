# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/tools/node.py
# module: src.proxmox_mcp.tools.node
# qname: src.proxmox_mcp.tools.node.NodeTools.get_node_status
# lines: 97-135
    def get_node_status(self, node: str) -> List[Content]:
        """Get detailed status information for a specific node.

        Retrieves comprehensive status information including:
        - CPU usage and configuration
        - Memory utilization details
        - Uptime and load statistics
        - Network status
        - Storage health
        - Running tasks and services

        Args:
            node: Name/ID of node to query (e.g., 'pve1', 'proxmox-node2')

        Returns:
            List of Content objects containing detailed node status:
            {
                "uptime": seconds,
                "cpu": {
                    "usage": percentage,
                    "cores": count
                },
                "memory": {
                    "used": bytes,
                    "total": bytes,
                    "free": bytes
                },
                ...additional status fields
            }

        Raises:
            ValueError: If the specified node is not found
            RuntimeError: If status retrieval fails (node offline, network issues)
        """
        try:
            result = self.proxmox.nodes(node).status.get()
            return self._format_response((node, result), "node_status")
        except Exception as e:
            self._handle_error(f"get status for node {node}", e)