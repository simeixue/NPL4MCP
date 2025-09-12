# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/dbt-mcp/examples/openai_responses/main.py
# module: examples.openai_responses.main
# qname: examples.openai_responses.main.main
# lines: 8-35
def main():
    client = OpenAI()
    prod_environment_id = os.environ.get("DBT_PROD_ENV_ID", os.getenv("DBT_ENV_ID"))
    token = os.environ.get("DBT_TOKEN")
    host = os.environ.get("DBT_HOST", "cloud.getdbt.com")

    messages = []
    while True:
        user_message = input("User > ")
        messages.append({"role": "user", "content": user_message})
        response = client.responses.create(
            model="gpt-4o-mini",
            tools=[
                {
                    "type": "mcp",
                    "server_label": "dbt",
                    "server_url": f"https://{host}/api/ai/v1/mcp/",
                    "require_approval": "never",
                    "headers": {
                        "Authorization": f"token {token}",
                        "x-dbt-prod-environment-id": prod_environment_id,
                    },
                },  # type: ignore
            ],
            input=messages,
        )
        messages.append({"role": "assistant", "content": response.output_text})
        print(f"Assistant > {response.output_text}")