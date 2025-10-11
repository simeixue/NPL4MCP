# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/examples/streamable_http_client.py
# module: examples.streamable_http_client
# qname: examples.streamable_http_client.main
# lines: 9-39
async def main():
    async with streamablehttp_client("http://localhost:8000/mcp") as (read_stream, write_stream, _):
        async with ClientSession(read_stream, write_stream) as session:
            print("Initializing session...")
            await session.initialize()
            print("Session initialized")

            # Scan code for security issues
            results = await session.call_tool(
                "semgrep_scan",
                {
                    "code_files": [
                        {
                            "path": "hello_world.py",
                            "content": "def hello(): print('Hello, World!')",
                        }
                    ]
                },
            )
            print("\n\nWe have results!\n")
            print("Raw result object:")
            print("=" * 80)
            print(results)
            print("\n\nPretty-printed result from semgrep_scan:")
            print("=" * 80)
            if isinstance(results.content[0], TextContent):
                print(json.dumps(json.loads(results.content[0].text), indent=2))
            else:
                print(f"First content is not TextContent: {type(results.content[0])}")
            print("\n\n")
            print("Hope that was helpful!")