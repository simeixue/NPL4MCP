# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/Medical_calculator_MCP/server.py
# module: server
# qname: server.bmi_calculator
# lines: 49-54
def bmi_calculator(weight_kg: float, height_m: float) -> float:
    """
    Calculates Body Mass Index (BMI)
    Formula: BMI = weight (kg) / height^2 (m)
    """
    return weight_kg / (height_m * height_m)