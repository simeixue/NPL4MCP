# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/formatting/templates.py
# module: src.proxmox_mcp.formatting.templates
# qname: src.proxmox_mcp.formatting.templates.ProxmoxTemplates.node_status
# lines: 60-95
    def node_status(node: str, status: Dict[str, Any]) -> str:
        """Template for detailed node status output.
        
        Args:
            node: Node name
            status: Node status data
            
        Returns:
            Formatted node status string
        """
        memory = status.get("memory", {})
        memory_used = memory.get("used", 0)
        memory_total = memory.get("total", 0)
        memory_percent = (memory_used / memory_total * 100) if memory_total > 0 else 0
        
        result = [
            f"{ProxmoxTheme.RESOURCES['node']} Node: {node}",
            f"  • Status: {status.get('status', 'unknown').upper()}",
            f"  • Uptime: {ProxmoxFormatters.format_uptime(status.get('uptime', 0))}",
            f"  • CPU Cores: {status.get('maxcpu', 'N/A')}",
            f"  • Memory: {ProxmoxFormatters.format_bytes(memory_used)} / "
            f"{ProxmoxFormatters.format_bytes(memory_total)} ({memory_percent:.1f}%)"
        ]
        
        # Add disk usage if available
        disk = status.get("disk", {})
        if disk:
            disk_used = disk.get("used", 0)
            disk_total = disk.get("total", 0)
            disk_percent = (disk_used / disk_total * 100) if disk_total > 0 else 0
            result.append(
                f"  • Disk: {ProxmoxFormatters.format_bytes(disk_used)} / "
                f"{ProxmoxFormatters.format_bytes(disk_total)} ({disk_percent:.1f}%)"
            )
        
        return "\n".join(result)