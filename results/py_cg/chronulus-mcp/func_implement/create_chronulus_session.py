# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/chronulus-mcp/src/chronulus_mcp/session.py
# module: src.chronulus_mcp.session
# qname: src.chronulus_mcp.session.create_chronulus_session
# lines: 8-42
async def create_chronulus_session(
        name: Annotated[str, Field(description="A short descriptive name for the use case defined in the session.")],
        situation: Annotated[str, Field(description="The broader context for the use case")],
        task: Annotated[str, Field(description="Specific details on the forecasting or prediction task.")],
        ctx: Context
) -> str:
    """Creates a new Chronulus Session

    A Chronulus Session allows you to use Chronulus Agents. To create a session, you need to provide a situation
    and task. Once created, this will generate a unique session id that can be used to when calling the agents.

    Args:
        name (str): A short descriptive name for the use case defined in the session.
        situation (str): The broader context for the use case.
        task (str): The specific prediction task.


    Returns:
        str: The session ID.
    """

    try:
        chronulus_session = Session(
            name=name,
            situation=situation,
            task=task,
            verbose=False,
        )

    except Exception as e:
        error_message = f"Failed to create chronulus session with the following error: \n\n{e}"
        _ = await ctx.error(message=error_message)
        return error_message

    return chronulus_session.session_id