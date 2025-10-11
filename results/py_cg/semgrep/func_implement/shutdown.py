# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/semgrep.py
# module: src.semgrep_mcp.semgrep
# qname: src.semgrep_mcp.semgrep.SemgrepContext.shutdown
# lines: 123-125
    def shutdown(self) -> None:
        if self.process is not None:
            self.process.terminate()