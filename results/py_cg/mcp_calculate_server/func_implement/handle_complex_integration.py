# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp_calculate_server/server.py
# module: server
# qname: server.handle_complex_integration
# lines: 66-131
def handle_complex_integration(expression, locals_dict):
    """Handle complex integral expressions"""
    try:
        # Check if it's an infinite integral
        if "-oo" in expression or "oo" in expression:
            # Try symbolic computation
            expr = eval(expression, globals(), locals_dict)

            # If it's an integral object but not computed
            if isinstance(expr, sp.Integral):
                try:
                    # Try to perform the integral
                    result = expr.doit()

                    # Try to compute numerical result
                    try:
                        numerical = result.evalf()
                        return str(numerical)
                    except:
                        return str(result)
                except Exception as e:
                    # If symbolic integration fails, try alternative methods
                    try:
                        # Extract integral expression information
                        match = re.search(r"integrate\((.*?), \((.*?), (.*?), (.*?)\)\)", expression)
                        if match:
                            integrand, var, lower, upper = match.groups()

                            # For infinite integrals, use finite approximation
                            if (lower == "-oo" or lower == "oo") or (upper == "oo" or upper == "-oo"):
                                # Replace infinity with a large value
                                if lower == "-oo":
                                    lower = "-100"
                                elif lower == "oo":
                                    lower = "100"

                                if upper == "-oo":
                                    upper = "-100"
                                elif upper == "oo":
                                    upper = "100"

                                # Build finite range integral expression
                                finite_expr = f"integrate({integrand}, ({var}, {lower}, {upper}))"
                                result = eval(finite_expr, globals(), locals_dict)

                                try:
                                    numerical = result.evalf()
                                    return f"Approximate numerical result: {numerical} (using finite range integral)"
                                except:
                                    return f"Approximate result: {result} (using finite range integral)"
                    except Exception as e2:
                        return f"Integration error: {e}, finite approximation failed: {e2}"

            # Try to compute result directly
            try:
                numerical = expr.evalf()
                return str(numerical)
            except:
                return str(expr)

        # Regular integral
        result = eval(expression, globals(), locals_dict)
        return format_result(result)

    except Exception as e:
        return f"Integration error: {e}"