# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/oxylabs-mcp/tests/e2e/test_llm_agent.py
# module: tests.e2e.test_llm_agent
# qname: tests.e2e.test_llm_agent.get_models
# lines: 35-42
def get_models() -> list[str]:
    models = []

    for env_var, model_name in MODELS_CONFIG:
        if os.getenv(env_var):
            models.append(model_name)

    return models