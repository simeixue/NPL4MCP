# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/tracking/tracking.py
# module: src.dbt_mcp.tracking.tracking
# qname: src.dbt_mcp.tracking.tracking.UsageTracker.emit_tool_called_event
# lines: 28-65
    def emit_tool_called_event(
        self,
        config: TrackingConfig,
        tool_name: str,
        arguments: dict[str, Any],
        start_time_ms: int,
        end_time_ms: int,
        error_message: str | None = None,
    ):
        try:
            arguments_mapping: Mapping[str, str] = {
                k: json.dumps(v) for k, v in arguments.items()
            }

            log_proto(
                ToolCalled(
                    event_id=str(uuid.uuid4()),
                    start_time_ms=start_time_ms,
                    end_time_ms=end_time_ms,
                    tool_name=tool_name,
                    arguments=arguments_mapping,
                    error_message=error_message or "",
                    dbt_cloud_environment_id_dev=str(config.dev_environment_id)
                    if config.dev_environment_id
                    else "",
                    dbt_cloud_environment_id_prod=str(config.prod_environment_id)
                    if config.prod_environment_id
                    else "",
                    dbt_cloud_user_id=str(config.dbt_cloud_user_id)
                    if config.dbt_cloud_user_id
                    else "",
                    local_user_id=config.local_user_id or "",
                    host=config.host or "",
                    multicell_account_prefix=config.host_prefix or "",
                )
            )
        except Exception as e:
            logger.error(f"Error emitting tool called event: {e}")