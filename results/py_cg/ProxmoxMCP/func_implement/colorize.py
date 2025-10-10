# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/formatting/colors.py
# module: src.proxmox_mcp.formatting.colors
# qname: src.proxmox_mcp.formatting.colors.ProxmoxColors.colorize
# lines: 44-60
    def colorize(cls, text: str, color: str, style: Optional[str] = None) -> str:
        """Add color and optional style to text with theme awareness.
        
        Args:
            text: Text to colorize
            color: ANSI color code
            style: Optional ANSI style code
            
        Returns:
            Formatted text string
        """
        if not ProxmoxTheme.USE_COLORS:
            return text
            
        if style:
            return f"{style}{color}{text}{cls.RESET}"
        return f"{color}{text}{cls.RESET}"