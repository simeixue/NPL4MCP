# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/elevenlabs/elevenlabs_mcp/server.py
# module: elevenlabs_mcp.server
# qname: elevenlabs_mcp.server.get_agent
# lines: 685-703
def get_agent(agent_id: str) -> TextContent:
    """Get details about a specific conversational AI agent.

    Args:
        agent_id: The ID of the agent to retrieve

    Returns:
        TextContent with detailed information about the agent
    """
    response = client.conversational_ai.agents.get(agent_id=agent_id)

    voice_info = "None"
    if response.conversation_config.tts:
        voice_info = f"Voice ID: {response.conversation_config.tts.voice_id}"

    return TextContent(
        type="text",
        text=f"Agent Details: Name: {response.name}, Agent ID: {response.agent_id}, Voice Configuration: {voice_info}, Created At: {datetime.fromtimestamp(response.metadata.created_at_unix_secs).strftime('%Y-%m-%d %H:%M:%S')}",
    )