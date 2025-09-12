# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/chronulus-mcp/src/chronulus_mcp/agent/_types.py
# module: src.chronulus_mcp.agent._types
# qname: src.chronulus_mcp.agent._types.generate_model_from_fields
# lines: 26-65
def generate_model_from_fields(model_name: str, fields: List[InputField]) -> Type[BaseModel]:
    """
    Generate a new Pydantic BaseModel from a list of InputField objects.

    Args:
        model_name: The name for the generated model class
        fields: List of InputField objects defining the model's fields

    Returns:
        A new Pydantic BaseModel class with the specified fields
    """
    literal_type_mapping = {
        'str': str,
        'ImageFromFile': ImageFromFile,
        'List[ImageFromFile]': List[ImageFromFile],
        'TextFromFile': TextFromFile,
        'List[TextFromFile]': List[TextFromFile],
        'PdfFromFile': PdfFromFile,
        'List[PdfFromFile]': List[PdfFromFile]
    }

    field_definitions = {
        field.name: (
            Optional[literal_type_mapping.get(field.type, str)],
            Field(description=field.description)
        )
        for field in fields
    }

    DynamicModel = create_model(
        model_name,
        __base__=BaseModel,  # Explicitly set BaseModel as the base class
        **field_definitions
    )

    DynamicModel.__annotations__ = {
        field.name: str for field in fields
    }

    return DynamicModel