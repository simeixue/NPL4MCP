# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/src/dbt_mcp/dbt_cli/tools.py
# module: src.dbt_mcp.dbt_cli.tools
# qname: src.dbt_mcp.dbt_cli.tools.create_dbt_cli_tool_definitions._run_dbt_command
# lines: 18-84
    def _run_dbt_command(
        command: list[str],
        selector: str | None = None,
        resource_type: list[str] | None = None,
        is_selectable: bool = False,
        is_full_refresh: bool | None = False,
        vars: str | None = None,
    ) -> str:
        try:
            # Commands that should always be quiet to reduce output verbosity
            verbose_commands = [
                "build",
                "compile",
                "docs",
                "parse",
                "run",
                "test",
                "list",
            ]

            if is_full_refresh is True:
                command.append("--full-refresh")

            if vars and isinstance(vars, str):
                command.extend(["--vars", vars])

            if selector:
                selector_params = str(selector).split(" ")
                command.extend(["--select"] + selector_params)

            if isinstance(resource_type, Iterable):
                command.extend(["--resource-type"] + resource_type)

            full_command = command.copy()
            # Add --quiet flag to specific commands to reduce context window usage
            if len(full_command) > 0 and full_command[0] in verbose_commands:
                main_command = full_command[0]
                command_args = full_command[1:] if len(full_command) > 1 else []
                full_command = [main_command, "--quiet", *command_args]

            # We change the path only if this is an absolute path, otherwise we can have
            # problems with relative paths applied multiple times as DBT_PROJECT_DIR
            # is applied to dbt Core and Fusion as well (but not the dbt Cloud CLI)
            cwd_path = config.project_dir if os.path.isabs(config.project_dir) else None

            # Add appropriate color disable flag based on binary type
            color_flag = get_color_disable_flag(config.binary_type)
            args = [config.dbt_path, color_flag, *full_command]

            process = subprocess.Popen(
                args=args,
                cwd=cwd_path,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                stdin=subprocess.DEVNULL,
                text=True,
            )
            output, _ = process.communicate(timeout=config.dbt_cli_timeout)
            return output or "OK"
        except subprocess.TimeoutExpired:
            return "Timeout: dbt command took too long to complete." + (
                " Try using a specific selector to narrow down the results."
                if is_selectable
                else ""
            )
        except Exception as e:
            return str(e)