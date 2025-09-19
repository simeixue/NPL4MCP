# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/Medical_calculator_MCP/server.py
# module: server
# qname: server.corrected_calcium
# lines: 70-75
def corrected_calcium(calcium: float, albumin: float) -> float:
    """
    Calculates corrected calcium level
    Formula: Corrected calcium (mg/dL) = measured calcium (mg/dL) + 0.8 * (4.0 - albumin (g/dL))
    """
    return calcium + 0.8 * (4.0 - albumin)