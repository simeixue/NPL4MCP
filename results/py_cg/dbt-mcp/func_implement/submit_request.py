# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/semantic_layer/gql/gql_request.py
# module: src.dbt_mcp.semantic_layer.gql.gql_request
# qname: src.dbt_mcp.semantic_layer.gql.gql_request.submit_request
# lines: 7-17
def submit_request(
    sl_config: SemanticLayerConfig,
    payload: dict,
) -> dict:
    if "variables" not in payload:
        payload["variables"] = {}
    payload["variables"]["environmentId"] = sl_config.prod_environment_id
    r = requests.post(sl_config.url, json=payload, headers=sl_config.headers)
    result = r.json()
    raise_gql_error(result)
    return result