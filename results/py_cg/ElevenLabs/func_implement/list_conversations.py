# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/elevenlabs/elevenlabs_mcp/server.py
# module: elevenlabs_mcp.server
# qname: elevenlabs_mcp.server.list_conversations
# lines: 772-831
def list_conversations(
    agent_id: str | None = None,
    cursor: str | None = None,
    call_start_before_unix: int | None = None,
    call_start_after_unix: int | None = None,
    page_size: int = 30,
    max_length: int = 10000,
) -> TextContent:
    """List conversations with filtering options."""
    page_size = min(page_size, 100)

    try:
        response = client.conversational_ai.conversations.list(
            cursor=cursor,
            agent_id=agent_id,
            call_start_before_unix=call_start_before_unix,
            call_start_after_unix=call_start_after_unix,
            page_size=page_size,
        )

        if not response.conversations:
            return TextContent(type="text", text="No conversations found.")

        conv_list = []
        for conv in response.conversations:
            start_time = datetime.fromtimestamp(conv.start_time_unix_secs).strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            conv_info = f"""Conversation ID: {conv.conversation_id}
Status: {conv.status}
Agent: {conv.agent_name or 'N/A'} (ID: {conv.agent_id})
Started: {start_time}
Duration: {conv.call_duration_secs} seconds
Messages: {conv.message_count}
Call Successful: {conv.call_successful}"""

            conv_list.append(conv_info)

        formatted_list = "\n\n".join(conv_list)

        pagination_info = f"Showing {len(response.conversations)} conversations"
        if response.has_more:
            pagination_info += f" (more available, next cursor: {response.next_cursor})"

        full_text = f"{pagination_info}\n\n{formatted_list}"

        # Use utility to handle large text content
        result_text = handle_large_text(full_text, max_length, "conversation list")

        # If content was saved to file, prepend pagination info
        if result_text != full_text:
            result_text = f"{pagination_info}\n\n{result_text}"

        return TextContent(type="text", text=result_text)

    except Exception as e:
        make_error(f"Failed to list conversations: {str(e)}")
        # This line is unreachable but satisfies type checker
        return TextContent(type="text", text="")