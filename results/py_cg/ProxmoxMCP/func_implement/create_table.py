# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/formatting/components.py
# module: src.proxmox_mcp.formatting.components
# qname: src.proxmox_mcp.formatting.components.ProxmoxComponents.create_table
# lines: 12-82
    def create_table(headers: List[str], rows: List[List[str]], title: Optional[str] = None) -> str:
        """Create an ASCII table with optional title.
        
        Args:
            headers: List of column headers
            rows: List of row data
            title: Optional table title
            
        Returns:
            Formatted table string
        """
        # Calculate column widths considering multi-line content
        widths = [len(header) for header in headers]
        for row in rows:
            for i, cell in enumerate(row):
                cell_lines = str(cell).split('\n')
                max_line_length = max(len(line) for line in cell_lines)
                widths[i] = max(widths[i], max_line_length)
        
        # Create separator line
        separator = "+" + "+".join("-" * (w + 2) for w in widths) + "+"
        
        # Calculate total width for title
        total_width = sum(widths) + len(widths) + 1
        
        # Build table
        result = []
        
        # Add title if provided
        if title:
            # Center the title
            title_str = ProxmoxColors.colorize(title, ProxmoxColors.CYAN, ProxmoxColors.BOLD)
            padding = (total_width - len(title) - 2) // 2  # -2 for the border chars
            title_separator = "+" + "-" * (total_width - 2) + "+"
            result.extend([
                title_separator,
                "|" + " " * padding + title_str + " " * (total_width - padding - len(title) - 2) + "|",
                title_separator
            ])
        
        # Add headers
        header = "|" + "|".join(f" {ProxmoxColors.colorize(h, ProxmoxColors.CYAN):<{w}} " for w, h in zip(widths, headers)) + "|"
        result.extend([separator, header, separator])
        
        # Add rows with multi-line cell support
        for row in rows:
            # Split each cell into lines
            cell_lines = [str(cell).split('\n') for cell in row]
            max_lines = max(len(lines) for lines in cell_lines)
            
            # Pad cells with fewer lines
            padded_cells = []
            for lines in cell_lines:
                if len(lines) < max_lines:
                    lines.extend([''] * (max_lines - len(lines)))
                padded_cells.append(lines)
            
            # Create row strings for each line
            for line_idx in range(max_lines):
                line_parts = []
                for col_idx, cell_lines in enumerate(padded_cells):
                    line = cell_lines[line_idx]
                    line_parts.append(f" {line:<{widths[col_idx]}} ")
                result.append("|" + "|".join(line_parts) + "|")
            
            # Add separator after each row except the last
            if row != rows[-1]:
                result.append(separator)
        
        result.append(separator)
        return "\n".join(result)