# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dappier-mcp/src/dappier_mcp/server.py
# module: src.dappier_mcp.server
# qname: src.dappier_mcp.server.dappier_real_time_search
# lines: 17-50
def dappier_real_time_search(
    query: Annotated[str, Field(description="The search query to retrieve real-time information.")],
    ai_model_id: Annotated[
        Literal["am_01j06ytn18ejftedz6dyhz2b15", "am_01j749h8pbf7ns8r1bq9s2evrh"],
        Field(
            description=(
                "The AI model ID to use for the query.\n\n"
                "Available AI Models:\n"
                "- am_01j06ytn18ejftedz6dyhz2b15: (Real-Time Data) Access real-time Google web search results, including "
                "the latest news, stock market data, news, weather, travel, deals, and more. Use this model when no stock ticker symbol is provided.\n"
                "- am_01j749h8pbf7ns8r1bq9s2evrh: (Stock Market Data) Access real-time financial news, stock prices, "
                "and trades from Polygon.io, with AI-powered insights and up-to-the-minute updates. Use this model only when a stock ticker symbol is provided.\n\n"
            ),
        )
    ]
) -> str:
    """
    Retrieve real-time search data from Dappier by processing an AI model that supports two key capabilities:

    - Real-Time Web Search:  
    Access the latest news, stock market data, weather, travel information, deals, and more using model `am_01j06ytn18ejftedz6dyhz2b15`.  
    Use this model when no stock ticker symbol is provided.

    - Stock Market Data:  
    Retrieve real-time financial news, stock prices, and trade updates using model `am_01j749h8pbf7ns8r1bq9s2evrh`.  
    Use this model only when a stock ticker symbol is provided.

    Based on the provided `ai_model_id`, the tool selects the appropriate model and returns search results.
    """
    try:
        response = client.search_real_time_data(query=query, ai_model_id=ai_model_id)
        return response.message
    except Exception as e:
        return f"Error: {str(e)}"