# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/formatting/formatters.py
# module: src.proxmox_mcp.formatting.formatters
# qname: src.proxmox_mcp.formatting.formatters.ProxmoxFormatters.format_command_output
# lines: 129-157
    def format_command_output(success: bool, command: str, output: str, error: str = None) -> str:
        """Format command execution output.
        
        Args:
            success: Whether command succeeded
            command: The command that was executed
            output: Command output
            error: Optional error message
            
        Returns:
            Formatted command output string
        """
        result = [
            f"{ProxmoxTheme.ACTIONS['command']} Console Command Result",
            f"  • Status: {'SUCCESS' if success else 'FAILED'}",
            f"  • Command: {command}",
            "",
            "Output:",
            output.strip()
        ]
        
        if error:
            result.extend([
                "",
                "Error:",
                error.strip()
            ])
            
        return "\n".join(result)