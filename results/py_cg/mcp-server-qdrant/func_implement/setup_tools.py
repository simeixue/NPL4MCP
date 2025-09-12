# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-server-qdrant/src/mcp_server_qdrant/mcp_server.py
# module: src.mcp_server_qdrant.mcp_server
# qname: src.mcp_server_qdrant.mcp_server.QdrantMCPServer.setup_tools
# lines: 88-199
    def setup_tools(self):
        """
        Register the tools in the server.
        """

        async def store(
            ctx: Context,
            information: Annotated[str, Field(description="Text to store")],
            collection_name: Annotated[
                str, Field(description="The collection to store the information in")
            ],
            # The `metadata` parameter is defined as non-optional, but it can be None.
            # If we set it to be optional, some of the MCP clients, like Cursor, cannot
            # handle the optional parameter correctly.
            metadata: Annotated[
                Metadata | None,
                Field(
                    description="Extra metadata stored along with memorised information. Any json is accepted."
                ),
            ] = None,
        ) -> str:
            """
            Store some information in Qdrant.
            :param ctx: The context for the request.
            :param information: The information to store.
            :param metadata: JSON metadata to store with the information, optional.
            :param collection_name: The name of the collection to store the information in, optional. If not provided,
                                    the default collection is used.
            :return: A message indicating that the information was stored.
            """
            await ctx.debug(f"Storing information {information} in Qdrant")

            entry = Entry(content=information, metadata=metadata)

            await self.qdrant_connector.store(entry, collection_name=collection_name)
            if collection_name:
                return f"Remembered: {information} in collection {collection_name}"
            return f"Remembered: {information}"

        async def find(
            ctx: Context,
            query: Annotated[str, Field(description="What to search for")],
            collection_name: Annotated[
                str, Field(description="The collection to search in")
            ],
            query_filter: ArbitraryFilter | None = None,
        ) -> list[str] | None:
            """
            Find memories in Qdrant.
            :param ctx: The context for the request.
            :param query: The query to use for the search.
            :param collection_name: The name of the collection to search in, optional. If not provided,
                                    the default collection is used.
            :param query_filter: The filter to apply to the query.
            :return: A list of entries found or None.
            """

            # Log query_filter
            await ctx.debug(f"Query filter: {query_filter}")

            query_filter = models.Filter(**query_filter) if query_filter else None

            await ctx.debug(f"Finding results for query {query}")

            entries = await self.qdrant_connector.search(
                query,
                collection_name=collection_name,
                limit=self.qdrant_settings.search_limit,
                query_filter=query_filter,
            )
            if not entries:
                return None
            content = [
                f"Results for the query '{query}'",
            ]
            for entry in entries:
                content.append(self.format_entry(entry))
            return content

        find_foo = find
        store_foo = store

        filterable_conditions = (
            self.qdrant_settings.filterable_fields_dict_with_conditions()
        )

        if len(filterable_conditions) > 0:
            find_foo = wrap_filters(find_foo, filterable_conditions)
        elif not self.qdrant_settings.allow_arbitrary_filter:
            find_foo = make_partial_function(find_foo, {"query_filter": None})

        if self.qdrant_settings.collection_name:
            find_foo = make_partial_function(
                find_foo, {"collection_name": self.qdrant_settings.collection_name}
            )
            store_foo = make_partial_function(
                store_foo, {"collection_name": self.qdrant_settings.collection_name}
            )

        self.tool(
            find_foo,
            name="qdrant-find",
            description=self.tool_settings.tool_find_description,
        )

        if not self.qdrant_settings.read_only:
            # Those methods can modify the database
            self.tool(
                store_foo,
                name="qdrant-store",
                description=self.tool_settings.tool_store_description,
            )