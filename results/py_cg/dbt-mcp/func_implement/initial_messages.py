# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/evals/semantic_layer/test_eval_semantic_layer.py
# module: evals.semantic_layer.test_eval_semantic_layer
# qname: evals.semantic_layer.test_eval_semantic_layer.initial_messages
# lines: 139-145
def initial_messages(content: str) -> ResponseInputParam:
    return [
        {
            "role": "user",
            "content": content,
        }
    ]