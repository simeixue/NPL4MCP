# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/evals/semantic_layer/test_eval_semantic_layer.py
# module: evals.semantic_layer.test_eval_semantic_layer
# qname: evals.semantic_layer.test_eval_semantic_layer.deep_equal
# lines: 62-72
def deep_equal(dict1: Any, dict2: Any) -> bool:
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict1.keys() == dict2.keys() and all(
            deep_equal(dict1[k], dict2[k]) for k in dict1
        )
    elif isinstance(dict1, list) and isinstance(dict2, list):
        return len(dict1) == len(dict2) and all(
            deep_equal(x, y) for x, y in zip(dict1, dict2, strict=False)
        )
    else:
        return dict1 == dict2