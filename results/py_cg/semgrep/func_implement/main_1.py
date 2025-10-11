# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/semgrep/examples/sse_client.py
# module: examples.sse_client
# qname: examples.sse_client.main
# lines: 8-35
async def main():
    async with sse_client("http://localhost:8000/sse") as (read_stream, write_stream):
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
            print(json.dumps(json.loads(results.content[0].text), indent=2))
            print("\n\n")
            print("Hope that was helpful!")