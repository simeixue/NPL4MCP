# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/Medical_calculator_MCP/server.py
# module: server
# qname: server.glucose_unit_conversion_mmol_to_mg
# lines: 33-38
def glucose_unit_conversion_mmol_to_mg(glucose_mmol: float) -> float:
    """
    Converts glucose from mmol/L to mg/dL
    Formula: mg/dL = mmol/L × 18.0182
    """
    return glucose_mmol * 18.0182