# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/server.py
# module: src.meilisearch_mcp.server
# qname: src.meilisearch_mcp.server.MeilisearchMCPServer._setup_handlers.handle_list_tools
# lines: 72-460
        async def handle_list_tools() -> list[types.Tool]:
            """List available tools"""
            return [
                types.Tool(
                    name="get-connection-settings",
                    description="Get current Meilisearch connection settings",
                    inputSchema={
                        "type": "object",
                        "properties": {},
                        "additionalProperties": False,
                    },
                ),
                types.Tool(
                    name="update-connection-settings",
                    description="Update Meilisearch connection settings",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "url": {"type": "string"},
                            "api_key": {"type": "string"},
                        },
                        "additionalProperties": False,
                    },
                ),
                types.Tool(
                    name="health-check",
                    description="Check Meilisearch server health",
                    inputSchema={
                        "type": "object",
                        "properties": {},
                        "additionalProperties": False,
                    },
                ),
                types.Tool(
                    name="get-version",
                    description="Get Meilisearch version information",
                    inputSchema={
                        "type": "object",
                        "properties": {},
                        "additionalProperties": False,
                    },
                ),
                types.Tool(
                    name="get-stats",
                    description="Get database statistics",
                    inputSchema={
                        "type": "object",
                        "properties": {},
                        "additionalProperties": False,
                    },
                ),
                types.Tool(
                    name="create-index",
                    description="Create a new Meilisearch index",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "uid": {"type": "string"},
                            "primaryKey": {"type": "string"},
                        },
                        "required": ["uid"],
                        "additionalProperties": False,
                    },
                ),
                types.Tool(
                    name="list-indexes",
                    description="List all Meilisearch indexes",
                    inputSchema={
                        "type": "object",
                        "properties": {},
                        "additionalProperties": False,
                    },
                ),
                types.Tool(
                    name="delete-index",
                    description="Delete a Meilisearch index",
                    inputSchema={
                        "type": "object",
                        "properties": {"uid": {"type": "string"}},
                        "required": ["uid"],
                        "additionalProperties": False,
                    },
                ),
                types.Tool(
                    name="get-documents",
                    description="Get documents from an index",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "indexUid": {"type": "string"},
                            "offset": {"type": "integer"},
                            "limit": {"type": "integer"},
                        },
                        "required": ["indexUid"],
                        "additionalProperties": False,
                    },
                ),
                types.Tool(
                    name="add-documents",
                    description="Add documents to an index",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "indexUid": {"type": "string"},
                            "documents": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "additionalProperties": True,
                                },
                            },
                            "primaryKey": {"type": "string"},
                        },
                        "required": ["indexUid", "documents"],
                        "additionalProperties": False,
                    },
                ),
                types.Tool(
                    name="get-settings",
                    description="Get current settings for an index",
                    inputSchema={
                        "type": "object",
                        "properties": {"indexUid": {"type": "string"}},
                        "required": ["indexUid"],
                        "additionalProperties": False,
                    },
                ),
                types.Tool(
                    name="update-settings",
                    description="Update settings for an index",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "indexUid": {"type": "string"},
                            "settings": {
                                "type": "object",
                                "additionalProperties": True,
                            },
                        },
                        "required": ["indexUid", "settings"],
                        "additionalProperties": False,
                    },
                ),
                types.Tool(
                    name="search",
                    description="Search through Meilisearch indices. If indexUid is not provided, it will search across all indices.",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "query": {"type": "string"},
                            "indexUid": {"type": "string"},
                            "limit": {"type": "integer"},
                            "offset": {"type": "integer"},
                            "filter": {"type": "string"},
                            "sort": {
                                "type": "array",
                                "items": {"type": "string"},
                            },
                        },
                        "required": ["query"],
                        "additionalProperties": False,
                    },
                ),
                types.Tool(
                    name="get-task",
                    description="Get information about a specific task",
                    inputSchema={
                        "type": "object",
                        "properties": {"taskUid": {"type": "integer"}},
                        "required": ["taskUid"],
                        "additionalProperties": False,
                    },
                ),
                types.Tool(
                    name="get-tasks",
                    description="Get list of tasks with optional filters",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "limit": {"type": "integer"},
                            "from": {"type": "integer"},
                            "reverse": {"type": "boolean"},
                            "batchUids": {
                                "type": "array",
                                "items": {"type": "string"},
                            },
                            "uids": {
                                "type": "array",
                                "items": {"type": "integer"},
                            },
                            "canceledBy": {
                                "type": "array",
                                "items": {"type": "string"},
                            },
                            "types": {
                                "type": "array",
                                "items": {"type": "string"},
                            },
                            "statuses": {
                                "type": "array",
                                "items": {"type": "string"},
                            },
                            "indexUids": {
                                "type": "array",
                                "items": {"type": "string"},
                            },
                            "afterEnqueuedAt": {"type": "string"},
                            "beforeEnqueuedAt": {"type": "string"},
                            "afterStartedAt": {"type": "string"},
                            "beforeStartedAt": {"type": "string"},
                            "afterFinishedAt": {"type": "string"},
                            "beforeFinishedAt": {"type": "string"},
                        },
                        "additionalProperties": False,
                    },
                ),
                types.Tool(
                    name="cancel-tasks",
                    description="Cancel tasks based on filters",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "uids": {"type": "string"},
                            "indexUids": {"type": "string"},
                            "types": {"type": "string"},
                            "statuses": {"type": "string"},
                        },
                        "additionalProperties": False,
                    },
                ),
                types.Tool(
                    name="get-keys",
                    description="Get list of API keys",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "offset": {"type": "integer"},
                            "limit": {"type": "integer"},
                        },
                        "additionalProperties": False,
                    },
                ),
                types.Tool(
                    name="create-key",
                    description="Create a new API key",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "description": {"type": "string"},
                            "actions": {"type": "array", "items": {"type": "string"}},
                            "indexes": {"type": "array", "items": {"type": "string"}},
                            "expiresAt": {"type": "string"},
                        },
                        "required": ["actions", "indexes"],
                        "additionalProperties": False,
                    },
                ),
                types.Tool(
                    name="delete-key",
                    description="Delete an API key",
                    inputSchema={
                        "type": "object",
                        "properties": {"key": {"type": "string"}},
                        "required": ["key"],
                        "additionalProperties": False,
                    },
                ),
                types.Tool(
                    name="get-health-status",
                    description="Get comprehensive health status of Meilisearch",
                    inputSchema={
                        "type": "object",
                        "properties": {},
                        "additionalProperties": False,
                    },
                ),
                types.Tool(
                    name="get-index-metrics",
                    description="Get detailed metrics for an index",
                    inputSchema={
                        "type": "object",
                        "properties": {"indexUid": {"type": "string"}},
                        "required": ["indexUid"],
                        "additionalProperties": False,
                    },
                ),
                types.Tool(
                    name="get-system-info",
                    description="Get system-level information",
                    inputSchema={
                        "type": "object",
                        "properties": {},
                        "additionalProperties": False,
                    },
                ),
                types.Tool(
                    name="create-chat-completion",
                    description="Create a conversational chat completion using Meilisearch's chat feature",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "workspace_uid": {
                                "type": "string",
                                "description": "Unique identifier of the chat workspace",
                            },
                            "messages": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "role": {
                                            "type": "string",
                                            "enum": ["user", "assistant", "system"],
                                        },
                                        "content": {"type": "string"},
                                    },
                                    "required": ["role", "content"],
                                },
                                "description": "List of message objects comprising the chat history",
                            },
                            "model": {
                                "type": "string",
                                "default": "gpt-3.5-turbo",
                                "description": "The model to use for completion",
                            },
                            "stream": {
                                "type": "boolean",
                                "default": True,
                                "description": "Whether to stream the response (currently must be true)",
                            },
                        },
                        "required": ["workspace_uid", "messages"],
                        "additionalProperties": False,
                    },
                ),
                types.Tool(
                    name="get-chat-workspaces",
                    description="Get list of available chat workspaces",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "offset": {
                                "type": "integer",
                                "description": "Number of workspaces to skip",
                            },
                            "limit": {
                                "type": "integer",
                                "description": "Maximum number of workspaces to return",
                            },
                        },
                        "additionalProperties": False,
                    },
                ),
                types.Tool(
                    name="get-chat-workspace-settings",
                    description="Get settings for a specific chat workspace",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "workspace_uid": {
                                "type": "string",
                                "description": "Unique identifier of the chat workspace",
                            },
                        },
                        "required": ["workspace_uid"],
                        "additionalProperties": False,
                    },
                ),
                types.Tool(
                    name="update-chat-workspace-settings",
                    description="Update settings for a specific chat workspace",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "workspace_uid": {
                                "type": "string",
                                "description": "Unique identifier of the chat workspace",
                            },
                            "settings": {
                                "type": "object",
                                "description": "Settings to update for the workspace",
                                "additionalProperties": True,
                            },
                        },
                        "required": ["workspace_uid", "settings"],
                        "additionalProperties": False,
                    },
                ),
            ]