# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/chronulus-mcp/src/chronulus_mcp/session.py
# module: src.chronulus_mcp.session
# qname: src.chronulus_mcp.session.get_risk_assessment_scorecard
# lines: 45-65
async def get_risk_assessment_scorecard(
        session_id: Annotated[str, Field(description="The session_id for the forecasting or prediction use case")],
        as_json:  Annotated[bool, Field(description="If true, returns the scorecard in JSON format, otherwise returns a markdown formatted scorecard")]
) -> str:
    """Get the risk assessment scorecard for the Session

    Args:
        session_id (str): The session_id for the forecasting or prediction use case.
        as_json (bool): If true, returns the scorecard in JSON format, otherwise returns a markdown formatted scorecard

    Returns:
        str: a risk assessment scorecard in the specified format.
    """

    chronulus_session = Session.load_from_saved_session(session_id=session_id, verbose=False)
    scorecard_md = chronulus_session.risk_scorecard(width='100%')
    if as_json:
        content = json.dumps(chronulus_session.scorecard.model_dump())
    else:
        content = scorecard_md
    return content