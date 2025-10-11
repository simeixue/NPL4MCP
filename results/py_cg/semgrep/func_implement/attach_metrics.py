# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/utilities/tracing.py
# module: src.semgrep_mcp.utilities.tracing
# qname: src.semgrep_mcp.utilities.tracing.attach_metrics
# lines: 73-89
def attach_metrics(
    span: trace.Span | None,
    version: str,
    skipped_rules: list[str],
    paths: list[Any],
    findings: list[dict[str, Any]],
    errors: list[dict[str, Any]],
    config: str | None,
):
    if span is None:
        return
    span.set_attribute("metrics.semgrep_version", version)
    span.set_attribute("metrics.num_skipped_rules", len(skipped_rules))
    span.set_attribute("metrics.rule_config", config if config else "default")
    span.set_attribute("metrics.num_scanned_files", len(paths))
    span.set_attribute("metrics.num_findings", len(findings))
    span.set_attribute("metrics.num_errors", len(errors))