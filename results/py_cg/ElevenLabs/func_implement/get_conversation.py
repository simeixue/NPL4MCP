# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/elevenlabs/elevenlabs_mcp/server.py
# module: elevenlabs_mcp.server
# qname: elevenlabs_mcp.server.get_conversation
# lines: 713-757
def get_conversation(
    conversation_id: str,
) -> TextContent:
    """Get conversation details with transcript"""
    try:
        response = client.conversational_ai.conversations.get(conversation_id)

        # Parse transcript using utility function
        transcript, _ = parse_conversation_transcript(response.transcript)

        response_text = f"""Conversation Details:
ID: {response.conversation_id}
Status: {response.status}
Agent ID: {response.agent_id}
Message Count: {len(response.transcript)}

Transcript:
{transcript}"""

        if response.metadata:
            metadata = response.metadata
            duration = getattr(
                metadata,
                "call_duration_secs",
                getattr(metadata, "duration_seconds", "N/A"),
            )
            started_at = getattr(
                metadata, "start_time_unix_secs", getattr(metadata, "started_at", "N/A")
            )
            response_text += (
                f"\n\nMetadata:\nDuration: {duration} seconds\nStarted: {started_at}"
            )

        if response.analysis:
            analysis_summary = getattr(
                response.analysis, "summary", "Analysis available but no summary"
            )
            response_text += f"\n\nAnalysis:\n{analysis_summary}"

        return TextContent(type="text", text=response_text)

    except Exception as e:
        make_error(f"Failed to fetch conversation: {str(e)}")
        # satisfies type checker
        return TextContent(type="text", text="")