# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/formatting/components.py
# module: src.proxmox_mcp.formatting.components
# qname: src.proxmox_mcp.formatting.components.ProxmoxComponents.create_key_value_grid
# lines: 127-158
    def create_key_value_grid(data: dict, columns: int = 2) -> str:
        """Create a grid of key-value pairs.
        
        Args:
            data: Dictionary of key-value pairs
            columns: Number of columns in grid
            
        Returns:
            Formatted grid string
        """
        # Calculate max widths for each column
        items = list(data.items())
        rows = [items[i:i + columns] for i in range(0, len(items), columns)]
        
        key_widths = [0] * columns
        val_widths = [0] * columns
        
        for row in rows:
            for i, (key, val) in enumerate(row):
                key_widths[i] = max(key_widths[i], len(str(key)))
                val_widths[i] = max(val_widths[i], len(str(val)))
        
        # Format rows
        result = []
        for row in rows:
            formatted_items = []
            for i, (key, val) in enumerate(row):
                key_str = ProxmoxColors.colorize(f"{key}:", ProxmoxColors.CYAN)
                formatted_items.append(f"{key_str:<{key_widths[i] + 10}} {val:<{val_widths[i]}}")
            result.append("  ".join(formatted_items))
        
        return "\n".join(result)