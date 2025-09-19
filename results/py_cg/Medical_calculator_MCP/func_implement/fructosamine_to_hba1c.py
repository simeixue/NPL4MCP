# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/Medical_calculator_MCP/server.py
# module: server
# qname: server.fructosamine_to_hba1c
# lines: 10-13
def fructosamine_to_hba1c(fructosamine: int) -> float:
    """Converts fructosamine to Hemoglobin A1c"""
    hba1c = ((0.017 * fructosamine) + 1.61)
    return hba1c