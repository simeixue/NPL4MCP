# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/elevenlabs/elevenlabs_mcp/server.py
# module: elevenlabs_mcp.server
# qname: elevenlabs_mcp.server.make_outbound_call
# lines: 971-998
def make_outbound_call(
    agent_id: str,
    agent_phone_number_id: str,
    to_number: str,
) -> TextContent:
    # Get phone number details to determine provider type
    phone_number = _get_phone_number_by_id(agent_phone_number_id)

    if phone_number.provider.lower() == "twilio":
        response = client.conversational_ai.twilio.outbound_call(
            agent_id=agent_id,
            agent_phone_number_id=agent_phone_number_id,
            to_number=to_number,
        )
        provider_info = "Twilio"
    elif phone_number.provider.lower() == "sip_trunk":
        response = client.conversational_ai.sip_trunk.outbound_call(
            agent_id=agent_id,
            agent_phone_number_id=agent_phone_number_id,
            to_number=to_number,
        )
        provider_info = "SIP trunk"
    else:
        make_error(f"Unsupported provider type: {phone_number.provider}")

    return TextContent(
        type="text", text=f"Outbound call initiated via {provider_info}: {response}."
    )