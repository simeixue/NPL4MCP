# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/chat.py
# module: src.meilisearch_mcp.chat
# qname: src.meilisearch_mcp.chat.ChatManager.create_chat_completion
# lines: 15-47
    async def create_chat_completion(
        self,
        workspace_uid: str,
        messages: List[Dict[str, str]],
        model: str = "gpt-3.5-turbo",
        stream: bool = True,
    ) -> str:
        try:
            logger.info(f"Creating chat completion for workspace: {workspace_uid}")

            # The SDK returns an iterator for streaming responses
            response_chunks = []
            for chunk in self.client.create_chat_completion(
                workspace_uid=workspace_uid,
                messages=messages,
                model=model,
                stream=stream,
            ):
                response_chunks.append(chunk)

            # Combine all chunks into a complete response
            full_response = self._combine_chunks(response_chunks)
            logger.info(
                f"Chat completion created successfully for workspace: {workspace_uid}"
            )
            return full_response

        except MeilisearchApiError as e:
            logger.error(f"Meilisearch API error in create_chat_completion: {e}")
            raise
        except Exception as e:
            logger.error(f"Error in create_chat_completion: {e}")
            raise