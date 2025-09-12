# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp_calculate_server/server.py
# module: server
# qname: server.calculate_expression
# lines: 11-64
def calculate_expression(expression: str) -> str:
    """
calculate mathematical expressions using the `sympify` function from `sympy`, parse and compute the input mathematical expression string, supports direct calls to SymPy functions (automatically recognizes x, y, z as symbolic variables)
Parameters:
    expression (str): Mathematical expression, e.g., "223 - 344 * 6" or "sin(pi/2) + log(10)".Replace special symbols with approximate values, e.g., pi → 3.1415"
Example expressions:
    "2 + 3*5"                          # Basic arithmetic → 17
    "expand((x + 1)**2)"               # Expand → x² + 2x + 1
    "diff(sin(x), x)"                  # Derivative → cos(x)
    "integrate(exp(x), (x, 0, 1))"      # Definite integral → E - 1
    "solve(x**2 - 4, x)"               # Solve equation → [-2, 2]
    "limit(tan(x)/x, x, 0)"            # Limit → 1
    "Sum(k, (k, 1, 10)).doit()"        # Summation → 55
    "Matrix([[1, 2], [3, 4]]).inv()"   # Matrix inverse → [[-2, 1], [3/2, -1/2]]
    "simplify((x**2 - 1)/(x + 1))"     # Simplify → x - 1
    "factor(x**2 - 2*x - 15)"          # Factorize → (x - 5)(x + 3)
    "series(cos(x), x, 0, 4)"          # Taylor series → 1 - x²/2 + x⁴/24 + O(x⁴)
    "integrate(exp(-x**2)*sin(x), (x, -oo, oo))"  # Complex integral
    "solve([x**2 + y**2 - 1, x + y - 1], [x, y])"  # Solve system of equations
    "Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).eigenvals()"  # Matrix eigenvalues
Returns:
    str: Calculation result. If the expression cannot be parsed or computed, returns an error message (str).
"""
    try:
        # Define common symbolic variables
        x, y, z = sp.symbols('x y z')

        # Create local namespace containing all sympy functions and symbolic variables
        locals_dict = {**sp.__dict__, 'x': x, 'y': y, 'z': z}

        # Special handling for various types of expressions

        # 1. Handle complex integral expressions
        if "integrate" in expression and ("oo" in expression or "-oo" in expression):
            return handle_complex_integration(expression, locals_dict)

        # 2. Handle system of equations solving expressions
        elif "solve(" in expression and "[" in expression and "]" in expression:
            return handle_equation_solving(expression, locals_dict)

        # 3. Handle matrix eigenvalue calculation expressions
        elif "eigenvals" in expression or "eigenvects" in expression:
            return handle_matrix_eigenvalues(expression, locals_dict)

        # 4. General expression calculation
        else:
            # First try to evaluate the expression directly
            result = eval(expression, globals(), locals_dict)

            # Process based on result type
            return format_result(result)

    except Exception as e:
        return f"Error: {e}"