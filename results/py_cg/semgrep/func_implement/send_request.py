# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/semgrep.py
# module: src.semgrep_mcp.semgrep
# qname: src.semgrep_mcp.semgrep.SemgrepContext.send_request
# lines: 91-121
    async def send_request(self, request: str, **kwargs: Any) -> str:
        if self.is_hosted:
            error_string = """
                Cannot run semgrep scan via RPC because the MCP server is hosted.
                RPC is only available when the MCP server is running locally.
                Use the `semgrep_scan` tool instead.
                """
            raise McpError(ErrorData(code=INVALID_REQUEST, message=error_string))

        if not self.pro_engine_available:
            error_string = """
                Cannot run semgrep scan via RPC because the Pro Engine is not installed.
                Try running `semgrep install-semgrep-pro` to install it.
                """
            raise McpError(ErrorData(code=INVALID_REQUEST, message=error_string))

        payload = {"method": request, **kwargs}

        try:
            return await self.communicate(json.dumps(payload))
        except Exception as e:
            # TODO: move this code out of send_request, make a proper result
            # type and interpret at the call site
            # this is not specific to semgrep_scan_rpc, but it is for now!!!
            msg = f"""
              Error sending request to semgrep (RPC server may not be running): {e}.
              Try using `semgrep_scan` instead.
            """
            logging.error(msg)

            raise McpError(ErrorData(code=INTERNAL_ERROR, message=msg)) from e