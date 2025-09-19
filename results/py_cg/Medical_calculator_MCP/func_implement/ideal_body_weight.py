# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/Medical_calculator_MCP/server.py
# module: server
# qname: server.ideal_body_weight
# lines: 57-67
def ideal_body_weight(height_cm: float, is_male: bool) -> float:
    """
    Calculates Ideal Body Weight (IBW) in kg using the Devine formula
    For males: IBW = 50 + 2.3 × (height in inches - 60)
    For females: IBW = 45.5 + 2.3 × (height in inches - 60)
    """
    height_inches = height_cm / 2.54
    if is_male:
        return 50 + 2.3 * (height_inches - 60)
    else:
        return 45.5 + 2.3 * (height_inches - 60)