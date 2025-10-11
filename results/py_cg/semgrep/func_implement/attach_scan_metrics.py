# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/utilities/tracing.py
# module: src.semgrep_mcp.utilities.tracing
# qname: src.semgrep_mcp.utilities.tracing.attach_scan_metrics
# lines: 94-105
def attach_scan_metrics(span: trace.Span | None, results: SemgrepScanResult, config: str | None):
    if span is None:
        return
    attach_metrics(
        span,
        results.version,
        results.skipped_rules,
        results.paths["scanned"],
        results.results,
        results.errors,
        config,
    )