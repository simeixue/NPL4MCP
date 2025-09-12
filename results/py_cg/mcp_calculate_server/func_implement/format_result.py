# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp_calculate_server/server.py
# module: server
# qname: server.format_result
# lines: 167-227
def format_result(result):
    """Format output based on result type"""
    try:
        # Handle dictionary type results (e.g., eigenvalues)
        if isinstance(result, dict):
            formatted = "{"
            for key, value in result.items():
                # Try numerical computation
                try:
                    key_eval = key.evalf()
                except:
                    key_eval = key

                formatted += f"{key_eval}: {value}, "

            if formatted.endswith(", "):
                formatted = formatted[:-2]

            formatted += "}"
            return formatted

        # Handle list type results (e.g., solutions to equations)
        elif isinstance(result, list):
            formatted = "["
            for item in result:
                # Check if it's a tuple (e.g., coordinate points)
                if isinstance(item, tuple):
                    coords = []
                    for val in item:
                        # Try numerical computation
                        try:
                            val_eval = val.evalf()
                            coords.append(str(val_eval))
                        except:
                            coords.append(str(val))

                    formatted += "(" + ", ".join(coords) + "), "
                else:
                    # Try numerical computation
                    try:
                        item_eval = item.evalf()
                        formatted += f"{item_eval}, "
                    except:
                        formatted += f"{item}, "

            if formatted.endswith(", "):
                formatted = formatted[:-2]

            formatted += "]"
            return formatted

        # Other types of results
        else:
            # Try numerical computation
            try:
                return str(result.evalf())
            except:
                return str(result)

    except Exception as e:
        return f"Result formatting error: {e}, original result: {result}"