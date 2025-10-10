# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/tools/node.py
# module: src.proxmox_mcp.tools.node
# qname: src.proxmox_mcp.tools.node.NodeTools.get_nodes
# lines: 33-95
    def get_nodes(self) -> List[Content]:
        """List all nodes in the Proxmox cluster with detailed status.

        Retrieves comprehensive information for each node including:
        - Basic status (online/offline)
        - Uptime statistics
        - CPU configuration and count
        - Memory usage and capacity
        
        Implements a fallback mechanism that returns basic information
        if detailed status retrieval fails for any node.

        Returns:
            List of Content objects containing formatted node information:
            {
                "node": "node_name",
                "status": "online/offline",
                "uptime": seconds,
                "maxcpu": cpu_count,
                "memory": {
                    "used": bytes,
                    "total": bytes
                }
            }

        Raises:
            RuntimeError: If the cluster-wide node query fails
        """
        try:
            result = self.proxmox.nodes.get()
            nodes = []
            
            # Get detailed info for each node
            for node in result:
                node_name = node["node"]
                try:
                    # Get detailed status for each node
                    status = self.proxmox.nodes(node_name).status.get()
                    nodes.append({
                        "node": node_name,
                        "status": node["status"],
                        "uptime": status.get("uptime", 0),
                        "maxcpu": status.get("cpuinfo", {}).get("cpus", "N/A"),
                        "memory": {
                            "used": status.get("memory", {}).get("used", 0),
                            "total": status.get("memory", {}).get("total", 0)
                        }
                    })
                except Exception:
                    # Fallback to basic info if detailed status fails
                    nodes.append({
                        "node": node_name,
                        "status": node["status"],
                        "uptime": 0,
                        "maxcpu": "N/A",
                        "memory": {
                            "used": node.get("maxmem", 0) - node.get("mem", 0),
                            "total": node.get("maxmem", 0)
                        }
                    })
            return self._format_response(nodes, "nodes")
        except Exception as e:
            self._handle_error("get nodes", e)