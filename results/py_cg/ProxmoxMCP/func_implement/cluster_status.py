# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/formatting/templates.py
# module: src.proxmox_mcp.formatting.templates
# qname: src.proxmox_mcp.formatting.templates.ProxmoxTemplates.cluster_status
# lines: 189-213
    def cluster_status(status: Dict[str, Any]) -> str:
        """Template for cluster status output.
        
        Args:
            status: Cluster status data
            
        Returns:
            Formatted cluster status string
        """
        result = [f"{ProxmoxTheme.SECTIONS['configuration']} Proxmox Cluster"]
        
        # Basic cluster info
        result.extend([
            "",
            f"  • Name: {status.get('name', 'N/A')}",
            f"  • Quorum: {'OK' if status.get('quorum') else 'NOT OK'}",
            f"  • Nodes: {status.get('nodes', 0)}",
        ])
        
        # Add resource count if available
        resources = status.get('resources', [])
        if resources:
            result.append(f"  • Resources: {len(resources)}")
        
        return "\n".join(result)