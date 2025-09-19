# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/Medical_calculator_MCP/server.py
# module: server
# qname: server.calculate_egfr
# lines: 107-120
def calculate_egfr(creatinine: float, age: int, is_male: bool, is_black: bool) -> float:
    """
    Calculates estimated Glomerular Filtration Rate (eGFR) using the MDRD formula
    Formula: 175 × (Scr)^-1.154 × (Age)^-0.203 × (0.742 if female) × (1.212 if black)
    Where Scr is serum creatinine in mg/dL
    """
    egfr = 175 * (creatinine ** -1.154) * (age ** -0.203)
    
    if not is_male:
        egfr *= 0.742
    if is_black:
        egfr *= 1.212
    
    return egfr