# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/kagimcp/src/kagimcp/server.py
# module: src.kagimcp.server
# qname: src.kagimcp.server.kagi_summarizer
# lines: 83-119
def kagi_summarizer(
    url: str = Field(description="A URL to a document to summarize."),
    summary_type: Literal["summary", "takeaway"] = Field(
        default="summary",
        description="Type of summary to produce. Options are 'summary' for paragraph prose and 'takeaway' for a bulleted list of key points.",
    ),
    target_language: str | None = Field(
        default=None,
        description="Desired output language using language codes (e.g., 'EN' for English). If not specified, the document's original language influences the output.",
    ),
) -> str:
    """Summarize content from a URL using the Kagi Summarizer API. The Summarizer can summarize any document type (text webpage, video, audio, etc.)"""
    try:
        if not url:
            raise ValueError("Summarizer called with no URL.")

        engine = os.environ.get("KAGI_SUMMARIZER_ENGINE", "cecil")

        valid_engines = {"cecil", "agnes", "daphne", "muriel"}
        if engine not in valid_engines:
            raise ValueError(
                f"Summarizer configured incorrectly, invalid summarization engine set: {engine}. Must be one of the following: {valid_engines}"
            )

        engine = cast(Literal["cecil", "agnes", "daphne", "muriel"], engine)

        summary = kagi_client.summarize(
            url,
            engine=engine,
            summary_type=summary_type,
            target_language=target_language,
        )["data"]["output"]

        return summary

    except Exception as e:
        return f"Error: {str(e) or repr(e)}"