# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/semantic_layer/levenshtein.py
# module: src.dbt_mcp.semantic_layer.levenshtein
# qname: src.dbt_mcp.semantic_layer.levenshtein.get_misspellings
# lines: 52-71
def get_misspellings(
    targets: list[str],
    words: list[str],
    top_k: int | None = None,
) -> list[Misspelling]:
    misspellings = []
    for target in targets:
        if target not in words:
            misspellings.append(
                Misspelling(
                    word=target,
                    similar_words=get_closest_words(
                        target=target,
                        words=words,
                        top_k=top_k,
                        threshold=max(1, len(target) // 2),
                    ),
                )
            )
    return misspellings