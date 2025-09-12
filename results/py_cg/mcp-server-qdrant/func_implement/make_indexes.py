# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/src/mcp_server_qdrant/common/filters.py
# module: src.mcp_server_qdrant.common.filters
# qname: src.mcp_server_qdrant.common.filters.make_indexes
# lines: 175-194
def make_indexes(
    filterable_fields: dict[str, FilterableField],
) -> dict[str, models.PayloadSchemaType]:
    indexes = {}

    for field_name, field in filterable_fields.items():
        if field.field_type == "keyword":
            indexes[f"{METADATA_PATH}.{field_name}"] = models.PayloadSchemaType.KEYWORD
        elif field.field_type == "integer":
            indexes[f"{METADATA_PATH}.{field_name}"] = models.PayloadSchemaType.INTEGER
        elif field.field_type == "float":
            indexes[f"{METADATA_PATH}.{field_name}"] = models.PayloadSchemaType.FLOAT
        elif field.field_type == "boolean":
            indexes[f"{METADATA_PATH}.{field_name}"] = models.PayloadSchemaType.BOOL
        else:
            raise ValueError(
                f"Unsupported field type {field.field_type} for field {field_name}"
            )

    return indexes