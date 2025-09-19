# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/Medical_calculator_MCP/server.py
# module: server
# qname: server.glucose_unit_conversion_mg_to_mmol
# lines: 41-46
def glucose_unit_conversion_mg_to_mmol(glucose_mg: float) -> float:
    """
    Converts glucose from mg/dL to mmol/L
    Formula: mmol/L = mg/dL / 18.0182
    """
    return glucose_mg / 18.0182