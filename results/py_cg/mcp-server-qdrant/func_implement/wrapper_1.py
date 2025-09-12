# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/src/mcp_server_qdrant/common/func_tools.py
# module: src.mcp_server_qdrant.common.func_tools
# qname: src.mcp_server_qdrant.common.func_tools.make_partial_function.wrapper
# lines: 10-19
    def wrapper(*args, **kwargs):
        # Start with fixed values
        bound_args = dict(fixed_values)

        # Bind positional/keyword args from caller
        for name, value in zip(remaining_params, args):
            bound_args[name] = value
        bound_args.update(kwargs)

        return original_func(**bound_args)