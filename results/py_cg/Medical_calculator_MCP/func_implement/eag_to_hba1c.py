# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/Medical_calculator_MCP/server.py
# module: server
# qname: server.eag_to_hba1c
# lines: 25-30
def eag_to_hba1c(eag_mg_dl: float) -> float:
    """
    Converts estimated average glucose (eAG) in mg/dL to HbA1c
    Formula: HbA1c = (eAG + 46.7) / 28.7
    """
    return (eag_mg_dl + 46.7) / 28.7