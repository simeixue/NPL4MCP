# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/server.py
# module: src.meilisearch_mcp.server
# qname: src.meilisearch_mcp.server.MeilisearchMCPServer._setup_handlers.handle_call_tool
# lines: 463-779
        async def handle_call_tool(
            name: str, arguments: Optional[Dict[str, Any]] = None
        ) -> list[types.TextContent]:
            """Handle tool execution"""
            try:
                if name == "get-connection-settings":
                    return [
                        types.TextContent(
                            type="text",
                            text=f"Current connection settings:\nURL: {self.url}\nAPI Key: {'*' * 8 if self.api_key else 'Not set'}",
                        )
                    ]

                elif name == "update-connection-settings":
                    self.update_connection(
                        arguments.get("url"), arguments.get("api_key")
                    )
                    return [
                        types.TextContent(
                            type="text",
                            text=f"Successfully updated connection settings to URL: {self.url}",
                        )
                    ]

                elif name == "create-index":
                    result = self.meili_client.indexes.create_index(
                        arguments["uid"], arguments.get("primaryKey")
                    )
                    return [
                        types.TextContent(type="text", text=f"Created index: {result}")
                    ]

                elif name == "list-indexes":
                    indexes = self.meili_client.get_indexes()
                    formatted_json = json.dumps(
                        indexes, indent=2, default=json_serializer
                    )
                    return [
                        types.TextContent(
                            type="text", text=f"Indexes:\n{formatted_json}"
                        )
                    ]

                elif name == "delete-index":
                    result = self.meili_client.indexes.delete_index(arguments["uid"])
                    return [
                        types.TextContent(
                            type="text",
                            text=f"Successfully deleted index: {arguments['uid']}",
                        )
                    ]

                elif name == "get-documents":
                    # Use default values to fix None parameter issues (related to issue #17)
                    offset = arguments.get("offset", 0)
                    limit = arguments.get("limit", 20)
                    documents = self.meili_client.documents.get_documents(
                        arguments["indexUid"],
                        offset,
                        limit,
                    )
                    # Convert DocumentsResults object to proper JSON format (fixes issue #16)
                    formatted_json = json.dumps(
                        documents, indent=2, default=json_serializer
                    )
                    return [
                        types.TextContent(
                            type="text", text=f"Documents:\n{formatted_json}"
                        )
                    ]

                elif name == "add-documents":
                    result = self.meili_client.documents.add_documents(
                        arguments["indexUid"],
                        arguments["documents"],
                        arguments.get("primaryKey"),
                    )
                    return [
                        types.TextContent(
                            type="text", text=f"Added documents: {result}"
                        )
                    ]

                elif name == "health-check":
                    is_healthy = self.meili_client.health_check()
                    return [
                        types.TextContent(
                            type="text",
                            text=f"Meilisearch is {is_healthy and 'available' or 'unavailable'}",
                        )
                    ]

                elif name == "get-version":
                    version = self.meili_client.get_version()
                    return [
                        types.TextContent(type="text", text=f"Version info: {version}")
                    ]

                elif name == "get-stats":
                    stats = self.meili_client.get_stats()
                    return [
                        types.TextContent(type="text", text=f"Database stats: {stats}")
                    ]

                elif name == "get-settings":
                    settings = self.meili_client.settings.get_settings(
                        arguments["indexUid"]
                    )
                    return [
                        types.TextContent(
                            type="text", text=f"Current settings: {settings}"
                        )
                    ]

                elif name == "update-settings":
                    result = self.meili_client.settings.update_settings(
                        arguments["indexUid"], arguments["settings"]
                    )
                    return [
                        types.TextContent(
                            type="text", text=f"Settings updated: {result}"
                        )
                    ]

                elif name == "search":
                    search_results = self.meili_client.search(
                        query=arguments["query"],
                        index_uid=arguments.get("indexUid"),
                        limit=arguments.get("limit"),
                        offset=arguments.get("offset"),
                        filter=arguments.get("filter"),
                        sort=arguments.get("sort"),
                    )

                    # Format the results for better readability
                    formatted_results = json.dumps(
                        search_results, indent=2, default=json_serializer
                    )
                    return [
                        types.TextContent(
                            type="text",
                            text=f"Search results for '{arguments['query']}':\n{formatted_results}",
                        )
                    ]

                elif name == "get-task":
                    task = self.meili_client.tasks.get_task(arguments["taskUid"])
                    return [
                        types.TextContent(type="text", text=f"Task information: {task}")
                    ]

                elif name == "get-tasks":
                    # Filter out any invalid parameters
                    valid_params = {
                        "limit",
                        "from",
                        "reverse",
                        "batchUids",
                        "uids",
                        "canceledBy",
                        "types",
                        "statuses",
                        "indexUids",
                        "afterEnqueuedAt",
                        "beforeEnqueuedAt",
                        "afterStartedAt",
                        "beforeStartedAt",
                        "afterFinishedAt",
                        "beforeFinishedAt",
                    }
                    filtered_args = (
                        {k: v for k, v in arguments.items() if k in valid_params}
                        if arguments
                        else {}
                    )
                    tasks = self.meili_client.tasks.get_tasks(filtered_args)
                    return [types.TextContent(type="text", text=f"Tasks: {tasks}")]

                elif name == "cancel-tasks":
                    result = self.meili_client.tasks.cancel_tasks(arguments)
                    return [
                        types.TextContent(
                            type="text", text=f"Tasks cancelled: {result}"
                        )
                    ]

                elif name == "get-keys":
                    keys = self.meili_client.keys.get_keys(arguments)
                    return [types.TextContent(type="text", text=f"API keys: {keys}")]

                elif name == "create-key":
                    key = self.meili_client.keys.create_key(
                        {
                            "description": arguments.get("description"),
                            "actions": arguments["actions"],
                            "indexes": arguments["indexes"],
                            "expiresAt": arguments.get("expiresAt"),
                        }
                    )
                    return [
                        types.TextContent(type="text", text=f"Created API key: {key}")
                    ]

                elif name == "delete-key":
                    self.meili_client.keys.delete_key(arguments["key"])
                    return [
                        types.TextContent(
                            type="text",
                            text=f"Successfully deleted API key: {arguments['key']}",
                        )
                    ]

                elif name == "get-health-status":
                    status = self.meili_client.monitoring.get_health_status()
                    self.logger.info("Health status checked", status=status.__dict__)
                    return [
                        types.TextContent(
                            type="text",
                            text=f"Health status: {json.dumps(status.__dict__, default=json_serializer)}",
                        )
                    ]

                elif name == "get-index-metrics":
                    metrics = self.meili_client.monitoring.get_index_metrics(
                        arguments["indexUid"]
                    )
                    self.logger.info(
                        "Index metrics retrieved",
                        index=arguments["indexUid"],
                        metrics=metrics.__dict__,
                    )
                    return [
                        types.TextContent(
                            type="text",
                            text=f"Index metrics: {json.dumps(metrics.__dict__, default=json_serializer)}",
                        )
                    ]

                elif name == "get-system-info":
                    info = self.meili_client.monitoring.get_system_information()
                    self.logger.info("System information retrieved", info=info)
                    return [
                        types.TextContent(
                            type="text", text=f"System information: {info}"
                        )
                    ]

                elif name == "create-chat-completion":
                    response = await self.chat_manager.create_chat_completion(
                        workspace_uid=arguments["workspace_uid"],
                        messages=arguments["messages"],
                        model=arguments.get("model", "gpt-3.5-turbo"),
                        stream=arguments.get("stream", True),
                    )
                    return [
                        types.TextContent(
                            type="text",
                            text=f"Chat completion response:\n{response}",
                        )
                    ]

                elif name == "get-chat-workspaces":
                    workspaces = await self.chat_manager.get_chat_workspaces(
                        offset=arguments.get("offset") if arguments else None,
                        limit=arguments.get("limit") if arguments else None,
                    )
                    formatted_json = json.dumps(
                        workspaces, indent=2, default=json_serializer
                    )
                    return [
                        types.TextContent(
                            type="text",
                            text=f"Chat workspaces:\n{formatted_json}",
                        )
                    ]

                elif name == "get-chat-workspace-settings":
                    settings = await self.chat_manager.get_chat_workspace_settings(
                        workspace_uid=arguments["workspace_uid"]
                    )
                    formatted_json = json.dumps(
                        settings, indent=2, default=json_serializer
                    )
                    return [
                        types.TextContent(
                            type="text",
                            text=f"Workspace settings for '{arguments['workspace_uid']}':\n{formatted_json}",
                        )
                    ]

                elif name == "update-chat-workspace-settings":
                    updated_settings = (
                        await self.chat_manager.update_chat_workspace_settings(
                            workspace_uid=arguments["workspace_uid"],
                            settings=arguments["settings"],
                        )
                    )
                    formatted_json = json.dumps(
                        updated_settings, indent=2, default=json_serializer
                    )
                    return [
                        types.TextContent(
                            type="text",
                            text=f"Updated workspace settings for '{arguments['workspace_uid']}':\n{formatted_json}",
                        )
                    ]

                raise ValueError(f"Unknown tool: {name}")

            except Exception as e:
                self.logger.error(
                    f"Error executing tool {name}",
                    error=str(e),
                    tool=name,
                    arguments=arguments,
                )
                return [types.TextContent(type="text", text=f"Error: {str(e)}")]