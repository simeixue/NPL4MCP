# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/formatting/theme.py
# module: src.proxmox_mcp.formatting.theme
# qname: src.proxmox_mcp.formatting.theme.ProxmoxTheme.get_section_emoji
# lines: 99-102
    def get_section_emoji(cls, section: str) -> str:
        """Get emoji for a section type with fallback."""
        section = section.lower()
        return cls.SECTIONS.get(section, cls.SECTIONS['details'])