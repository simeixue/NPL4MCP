# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/meilisearch-mcp/src/meilisearch_mcp/tasks.py
# module: src.meilisearch_mcp.tasks
# qname: src.meilisearch_mcp.tasks.serialize_task_results
# lines: 6-14
def serialize_task_results(obj: Any) -> Any:
    """Serialize task results into JSON-compatible format"""
    if hasattr(obj, "__dict__"):
        return {k: serialize_task_results(v) for k, v in obj.__dict__.items()}
    elif isinstance(obj, (list, tuple)):
        return [serialize_task_results(item) for item in obj]
    elif isinstance(obj, datetime):
        return obj.isoformat()
    return obj