# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/mcp-metricool/src/mcp_metricool/tools/tools.py
# module: src.mcp_metricool.tools.tools
# qname: src.mcp_metricool.tools.tools.get_metrics
# lines: 690-704
async def get_metrics(network: str) -> str | dict[str, Any]:
    """
    Retrieve the available metrics for a specific network.
    Args:
        network: Specific network to get the available metrics.
    """
    if network not in network_subject_metrics:
        return f"Incorrect network '{network}'. The available networks are: {', '.join(network_subject_metrics.keys())}"
    else:
        metrics = {}
        subjects = list(network_subject_metrics[network].keys())
        for subj in subjects:
            metrics[subj] = network_subject_metrics[network][subj]
        return {"metrics": metrics,
                "instructions": "Stop the chat, show the metrics and let the user choose the metrics they want to analyze before going again to get_analytics, the user must choose before you continue."}