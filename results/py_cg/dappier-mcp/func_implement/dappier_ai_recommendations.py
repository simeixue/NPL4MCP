# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dappier-mcp/src/dappier_mcp/server.py
# module: src.dappier_mcp.server
# qname: src.dappier_mcp.server.dappier_ai_recommendations
# lines: 54-141
def dappier_ai_recommendations(
    query: Annotated[
        str, 
        Field(description="The input string for AI-powered content recommendations.")
    ],
    data_model_id: Annotated[
        Literal[
            "dm_01j0pb465keqmatq9k83dthx34",
            "dm_01j0q82s4bfjmsqkhs3ywm3x6y",
            "dm_01j1sz8t3qe6v9g8ad102kvmqn",
            "dm_01j1sza0h7ekhaecys2p3y0vmj",
            "dm_01j5xy9w5sf49bm6b1prm80m27",
            "dm_01jagy9nqaeer9hxx8z1sk1jx6",
        ],
        Field(
            description=(
                "The data model ID to use for recommendations.\n\n"
                "Available Data Models:\n"
                "- dm_01j0pb465keqmatq9k83dthx34: (Sports News) Real-time news, updates, and personalized content "
                "from top sports sources like Sportsnaut, Forever Blueshirts, Minnesota Sports Fan, LAFB Network, "
                "Bounding Into Sports and Ringside Intel.\n"
                "- dm_01j0q82s4bfjmsqkhs3ywm3x6y: (Lifestyle News) Real-time updates, analysis, and personalized content "
                "from top sources like The Mix, Snipdaily, Nerdable and Familyproof.\n"
                "- dm_01j1sz8t3qe6v9g8ad102kvmqn: (iHeartDogs AI) A dog care expert with access to thousands of articles "
                "on health, behavior, lifestyle, grooming, ownership, and more from the industry-leading pet community "
                "iHeartDogs.com.\n"
                "- dm_01j1sza0h7ekhaecys2p3y0vmj: (iHeartCats AI) A cat care expert with access to thousands of articles on "
                "health, behavior, lifestyle, grooming, ownership, and more from the industry-leading pet community "
                "iHeartCats.com.\n"
                "- dm_01j5xy9w5sf49bm6b1prm80m27: (GreenMonster) A helpful guide to making conscious and compassionate "
                "choices that benefit people, animals, and the planet.\n"
                "- dm_01jagy9nqaeer9hxx8z1sk1jx6: (WISH-TV AI) Covers sports, politics, breaking news, multicultural news, "
                "Hispanic language content, entertainment, health, and education.\n\n"
            ),
        )
    ],
    similarity_top_k: Annotated[
        int, 
        Field(default=9, description="Number of top similar articles to retrieve based on semantic similarity.")
    ] = 9,
    ref: Annotated[
        Optional[str],
        Field(default=None, description="The site domain where recommendations should be prioritized.")
    ] = None,
    num_articles_ref: Annotated[
        int,
        Field(default=0, description="Minimum number of articles to return from the reference domain.")
    ] = 0,
    search_algorithm: Annotated[
        Literal["most_recent", "semantic", "most_recent_semantic", "trending"],
        Field(default="most_recent", description="The search algorithm to use for retrieving articles.")
    ] = "most_recent"
) -> str:
    """
    Fetch AI-powered recommendations from Dappier by processing the provided query with a selected data model that tailors results to specific interests.

    - **Sports News (dm_01j0pb465keqmatq9k83dthx34):**  
    Get real-time news, updates, and personalized content from top sports sources.

    - **Lifestyle News (dm_01j0q82s4bfjmsqkhs3ywm3x6y):**  
    Access current lifestyle updates, analysis, and insights from leading lifestyle publications.

    - **iHeartDogs AI (dm_01j1sz8t3qe6v9g8ad102kvmqn):**  
    Tap into a dog care expert with access to thousands of articles covering pet health, behavior, grooming, and ownership.

    - **iHeartCats AI (dm_01j1sza0h7ekhaecys2p3y0vmj):**  
    Utilize a cat care specialist that provides comprehensive content on cat health, behavior, and lifestyle.

    - **GreenMonster (dm_01j5xy9w5sf49bm6b1prm80m27):**  
    Receive guidance for making conscious and compassionate choices benefiting people, animals, and the planet.

    - **WISH-TV AI (dm_01jagy9nqaeer9hxx8z1sk1jx6):**  
    Get recommendations covering sports, breaking news, politics, multicultural updates, and more.

    Based on the chosen `data_model_id`, the tool processes the input query and returns a formatted summary including article titles, summaries, images, source URLs, publication dates, and relevance scores.
    """
    try:
        response = client.get_ai_recommendations(
            query=query,
            data_model_id=data_model_id,
            similarity_top_k=similarity_top_k,
            ref=ref or "",
            num_articles_ref=num_articles_ref,
            search_algorithm=search_algorithm,
        )
        return format_results(response)
    except Exception as e:
        return f"Error: {str(e)}"