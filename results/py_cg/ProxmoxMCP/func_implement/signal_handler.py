# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/ProxmoxMCP/src/proxmox_mcp/server.py
# module: src.proxmox_mcp.server
# qname: src.proxmox_mcp.server.ProxmoxMCPServer.start.signal_handler
# lines: 130-132
        def signal_handler(signum, frame):
            self.logger.info("Received signal to shutdown...")
            sys.exit(0)