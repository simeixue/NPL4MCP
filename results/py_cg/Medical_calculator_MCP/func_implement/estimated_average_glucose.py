# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/Medical_calculator_MCP/server.py
# module: server
# qname: server.estimated_average_glucose
# lines: 17-22
def estimated_average_glucose(hba1c: float) -> float:
    """
    Converts HbA1c to estimated average glucose (eAG) in mg/dL
    Formula: eAG (mg/dL) = 28.7 × HbA1c − 46.7
    """
    return (28.7 * hba1c) - 46.7