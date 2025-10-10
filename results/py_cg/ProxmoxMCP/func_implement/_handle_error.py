# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/tools/base.py
# module: src.proxmox_mcp.tools.base
# qname: src.proxmox_mcp.tools.base.ProxmoxTool._handle_error
# lines: 80-106
    def _handle_error(self, operation: str, error: Exception) -> None:
        """Handle and log errors from Proxmox operations.

        Provides standardized error handling across all tools by:
        - Logging errors with appropriate context
        - Categorizing errors into specific exception types
        - Converting Proxmox-specific errors into standard Python exceptions

        Args:
            operation: Description of the operation that failed (e.g., "get node status")
            error: The exception that occurred during the operation

        Raises:
            ValueError: For invalid input, missing resources, or permission issues
            RuntimeError: For unexpected errors or API failures
        """
        error_msg = str(error)
        self.logger.error(f"Failed to {operation}: {error_msg}")

        if "not found" in error_msg.lower():
            raise ValueError(f"Resource not found: {error_msg}")
        if "permission denied" in error_msg.lower():
            raise ValueError(f"Permission denied: {error_msg}")
        if "invalid" in error_msg.lower():
            raise ValueError(f"Invalid input: {error_msg}")
        
        raise RuntimeError(f"Failed to {operation}: {error_msg}")