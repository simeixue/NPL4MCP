# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/utilities/tracing.py
# module: src.semgrep_mcp.utilities.tracing
# qname: src.semgrep_mcp.utilities.tracing.get_deployment_id_from_token
# lines: 42-57
def get_deployment_id_from_token(token: str) -> str:
    """
    Returns the deployment ID the token is for, if token is valid
    """
    if not token:
        return ""

    resp = httpx.get(
        f"{SEMGREP_URL}{DEPLOYMENT_ROUTE}",
        headers={"Authorization": f"Bearer {token}"},
    )
    if resp.status_code == 200:
        deployment = resp.json().get("deployment")
        return deployment.get("id") if deployment else ""
    else:
        return ""