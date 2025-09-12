# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/semantic_layer/levenshtein.py
# module: src.dbt_mcp.semantic_layer.levenshtein
# qname: src.dbt_mcp.semantic_layer.levenshtein.get_closest_words
# lines: 30-49
def get_closest_words(
    target: str,
    words: list[str],
    top_k: int | None = None,
    threshold: int | None = None,
) -> list[str]:
    distances = [(word, levenshtein(target, word)) for word in words]

    # Filter by threshold if provided
    if threshold is not None:
        distances = [(word, dist) for word, dist in distances if dist <= threshold]

    # Sort by distance
    distances.sort(key=lambda x: x[1])

    # Limit by top_k if provided
    if top_k is not None:
        distances = distances[:top_k]

    return [word for word, _ in distances]