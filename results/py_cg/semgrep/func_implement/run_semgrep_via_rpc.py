# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/semgrep.py
# module: src.semgrep_mcp.semgrep
# qname: src.semgrep_mcp.semgrep.run_semgrep_via_rpc
# lines: 267-292
async def run_semgrep_via_rpc(context: SemgrepContext, data: list[CodeFile]) -> CliOutput:
    """
    Runs semgrep with the given arguments via RPC

    Args:
        data: List of code files to scan

    Returns:
        List of CliMatch objects
    """

    # TODO: to be honest it's silly for us to wire the contents of the files over RPC
    # if they exist on the local filesystem, we could just pass the paths
    files_json = [{"file": data.path, "content": data.content} for data in data]

    # ATD serialized value
    resp = await context.send_request("scanFiles", files=files_json)

    # The JSON we get is double encoded, looks like
    # '"{"results": ..., ...}"'
    # so we have to load it twice
    resp_json = json.loads(resp)
    resp_json = json.loads(resp_json)
    assert isinstance(resp_json, dict)

    return CliOutput.from_json(resp_json)