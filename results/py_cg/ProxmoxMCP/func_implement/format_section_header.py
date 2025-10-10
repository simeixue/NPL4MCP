# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/formatting/formatters.py
# module: src.proxmox_mcp.formatting.formatters
# qname: src.proxmox_mcp.formatting.formatters.ProxmoxFormatters.format_section_header
# lines: 97-110
    def format_section_header(title: str, section_type: str = 'header') -> str:
        """Format section header with emoji and border.
        
        Args:
            title: Section title
            section_type: Type of section for emoji selection
            
        Returns:
            Formatted section header
        """
        emoji = ProxmoxTheme.get_section_emoji(section_type)
        header = f"{emoji} {title}"
        border = "═" * len(header)
        return f"\n{header}\n{border}\n"