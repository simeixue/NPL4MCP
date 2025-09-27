# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/elevenlabs/elevenlabs_mcp/server.py
# module: elevenlabs_mcp.server
# qname: elevenlabs_mcp.server._get_phone_number_by_id
# lines: 948-954
def _get_phone_number_by_id(phone_number_id: str):
    """Helper function to get phone number details by ID."""
    phone_numbers = client.conversational_ai.phone_numbers.list()
    for phone in phone_numbers:
        if phone.phone_number_id == phone_number_id:
            return phone
    make_error(f"Phone number with ID {phone_number_id} not found.")