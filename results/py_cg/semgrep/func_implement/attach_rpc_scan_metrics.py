# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/utilities/tracing.py
# module: src.semgrep_mcp.utilities.tracing
# qname: src.semgrep_mcp.utilities.tracing.attach_rpc_scan_metrics
# lines: 108-119
def attach_rpc_scan_metrics(span: trace.Span | None, results: CliOutput):
    if span is None:
        return
    span.set_attribute(
        "metrics.semgrep_version", results.version.value if results.version else "unknown"
    )
    span.set_attribute("metrics.num_skipped_rules", len(results.skipped_rules))
    # Rules for RPC scans are cached by pulling the user's rules.
    span.set_attribute("metrics.rule_config", "cached")
    span.set_attribute("metrics.num_scanned_files", len(results.paths.scanned))
    span.set_attribute("metrics.num_findings", len(results.results))
    span.set_attribute("metrics.num_errors", len(results.errors))