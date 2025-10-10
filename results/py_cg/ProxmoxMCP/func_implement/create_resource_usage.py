# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/formatting/components.py
# module: src.proxmox_mcp.formatting.components
# qname: src.proxmox_mcp.formatting.components.ProxmoxComponents.create_resource_usage
# lines: 104-124
    def create_resource_usage(used: float, total: float, label: str, emoji: str) -> str:
        """Create a resource usage display with progress bar.
        
        Args:
            used: Used amount
            total: Total amount
            label: Resource label
            emoji: Resource emoji
            
        Returns:
            Formatted resource usage string
        """
        from .formatters import ProxmoxFormatters
        percentage = (used / total * 100) if total > 0 else 0
        progress = ProxmoxComponents.create_progress_bar(used, total)
        
        return (
            f"{emoji} {label}:\n"
            f"  {progress}\n"
            f"  {ProxmoxFormatters.format_bytes(used)} / {ProxmoxFormatters.format_bytes(total)}"
        )