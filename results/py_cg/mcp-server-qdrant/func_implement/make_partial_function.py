# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/src/mcp_server_qdrant/common/func_tools.py
# module: src.mcp_server_qdrant.common.func_tools
# qname: src.mcp_server_qdrant.common.func_tools.make_partial_function
# lines: 6-28
def make_partial_function(original_func: Callable, fixed_values: dict) -> Callable:
    sig = inspect.signature(original_func)

    @wraps(original_func)
    def wrapper(*args, **kwargs):
        # Start with fixed values
        bound_args = dict(fixed_values)

        # Bind positional/keyword args from caller
        for name, value in zip(remaining_params, args):
            bound_args[name] = value
        bound_args.update(kwargs)

        return original_func(**bound_args)

    # Only keep parameters NOT in fixed_values
    remaining_params = [name for name in sig.parameters if name not in fixed_values]
    new_params = [sig.parameters[name] for name in remaining_params]

    # Set the new __signature__ for introspection
    wrapper.__signature__ = sig.replace(parameters=new_params)  # type:ignore

    return wrapper