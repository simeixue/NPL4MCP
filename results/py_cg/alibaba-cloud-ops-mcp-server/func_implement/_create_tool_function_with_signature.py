# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/alibaba-cloud-ops-mcp-server/src/alibaba_cloud_ops_mcp_server/tools/api_tools.py
# module: src.alibaba_cloud_ops_mcp_server.tools.api_tools
# qname: src.alibaba_cloud_ops_mcp_server.tools.api_tools._create_tool_function_with_signature
# lines: 205-253
def _create_tool_function_with_signature(service: str, api: str, fields: dict, description: str):
    """
    Dynamically creates a lambda function with a custom signature based on the provided fields.
    """
    parameters = []
    annotations = {}
    defaults = {}

    for name, (type_, field_info) in fields.items():
        field_description = field_info.metadata.get('description', '')
        is_required = field_info.metadata.get('required', False)
        default_value = field_info.default if not is_required else ...

        field_default = Field(default=default_value, description=field_description)
        parameters.append(inspect.Parameter(
            name=name,
            kind=inspect.Parameter.POSITIONAL_OR_KEYWORD,
            default=field_default,
            annotation=type_
        ))
        annotations[name] = type_
        defaults[name] = field_default

    signature = inspect.Signature(parameters)
    function_name = f'{service.upper()}_{api}'
    def func_code(*args, **kwargs):
        bound_args = signature.bind(*args, **kwargs)
        bound_args.apply_defaults()

        return _tools_api_call(
            service=service,
            api=api,
            parameters=bound_args.arguments,
            ctx=None
        )

    func = types.FunctionType(
        func_code.__code__,
        globals(),
        function_name,
        None,
        func_code.__closure__
    )
    func.__signature__ = signature
    func.__annotations__ = annotations
    func.__defaults__ = tuple(defaults.values())
    func.__doc__ = description

    return func