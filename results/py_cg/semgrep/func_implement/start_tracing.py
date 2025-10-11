# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/src/semgrep_mcp/utilities/tracing.py
# module: src.semgrep_mcp.utilities.tracing
# qname: src.semgrep_mcp.utilities.tracing.start_tracing
# lines: 145-194
def start_tracing(name: str) -> Generator[trace.Span | None, None, None]:
    """Initialize OpenTelemetry tracing."""
    if tracing_disabled:
        yield None
    else:
        (endpoint, env) = get_trace_endpoint()

        token = os.environ.get("SEMGREP_APP_TOKEN", get_token_from_user_settings())

        # Create resource with basic attributes
        resource = Resource.create(
            {
                SERVICE_NAME: MCP_SERVICE_NAME,
                DEPLOYMENT_ENVIRONMENT: env,
                "metrics.semgrep_version": get_semgrep_version(),
                "metrics.mcp_version": __version__,
                "metrics.is_hosted": is_hosted(),
                "metrics.deployment_id": get_deployment_id_from_token(token),
            }
        )

        # Create tracer provider
        provider = TracerProvider(resource=resource)

        # Create OTLP exporter
        exporter = OTLPSpanExporter(endpoint=endpoint)

        # Create span processor
        processor = BatchSpanProcessor(exporter)
        provider.add_span_processor(processor)

        # Set the global tracer provider
        trace.set_tracer_provider(provider)

        # Get tracer instance
        tracer = trace.get_tracer(MCP_SERVICE_NAME)

        with tracer.start_as_current_span(name) as span:
            trace_id = trace.format_trace_id(span.get_span_context().trace_id)
            # Get a link to the trace in Datadog
            link = (
                f"(https://app.datadoghq.com/apm/trace/{trace_id})"
                if env != "semgrep-local"
                else ""
            )

            logging.info("Tracing initialized")
            logging.info(f"Tracing initialized with trace ID: {trace_id} {link}")

            yield span