# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/formatting/formatters.py
# module: src.proxmox_mcp.formatting.formatters
# qname: src.proxmox_mcp.formatting.formatters.ProxmoxFormatters.format_key_value
# lines: 113-126
    def format_key_value(key: str, value: str, emoji: str = "") -> str:
        """Format key-value pair with optional emoji.
        
        Args:
            key: Label/key
            value: Value to display
            emoji: Optional emoji prefix
            
        Returns:
            Formatted key-value string
        """
        key_str = ProxmoxColors.colorize(key, ProxmoxColors.CYAN)
        prefix = f"{emoji} " if emoji else ""
        return f"{prefix}{key_str}: {value}"