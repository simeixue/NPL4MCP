# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/src/mcp_server_qdrant/common/wrap_filters.py
# module: src.mcp_server_qdrant.common.wrap_filters
# qname: src.mcp_server_qdrant.common.wrap_filters.wrap_filters.wrapper
# lines: 21-31
    def wrapper(*args, **kwargs):
        # Start with fixed values
        filter_values = {}

        for field_name in filterable_fields:
            if field_name in kwargs:
                filter_values[field_name] = kwargs.pop(field_name)

        query_filter = make_filter(filterable_fields, filter_values)

        return original_func(**kwargs, query_filter=query_filter)