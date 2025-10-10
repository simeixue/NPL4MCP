# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/tools/cluster.py
# module: src.proxmox_mcp.tools.cluster
# qname: src.proxmox_mcp.tools.cluster.ClusterTools.get_cluster_status
# lines: 31-76
    def get_cluster_status(self) -> List[Content]:
        """Get overall Proxmox cluster health and configuration status.

        Retrieves comprehensive cluster information including:
        - Cluster name and identity
        - Quorum status (essential for cluster operations)
        - Active node count and health
        - Resource distribution and status
        
        This information is critical for:
        - Ensuring cluster stability
        - Monitoring node membership
        - Verifying resource availability
        - Detecting potential issues

        Returns:
            List of Content objects containing formatted cluster status:
            {
                "name": "cluster-name",
                "quorum": true/false,
                "nodes": count,
                "resources": [
                    {
                        "type": "resource-type",
                        "status": "status"
                    }
                ]
            }

        Raises:
            RuntimeError: If cluster status query fails due to:
                        - Network connectivity issues
                        - Authentication problems
                        - API endpoint failures
        """
        try:
            result = self.proxmox.cluster.status.get()
            status = {
                "name": result[0].get("name") if result else None,
                "quorum": result[0].get("quorate"),
                "nodes": len([node for node in result if node.get("type") == "node"]),
                "resources": [res for res in result if res.get("type") == "resource"]
            }
            return self._format_response(status, "cluster")
        except Exception as e:
            self._handle_error("get cluster status", e)