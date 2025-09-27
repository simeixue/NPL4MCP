# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/elevenlabs/elevenlabs_mcp/convai.py
# module: elevenlabs_mcp.convai
# qname: elevenlabs_mcp.convai.create_platform_settings
# lines: 62-86
def create_platform_settings(
    record_voice: bool,
    retention_days: int,
) -> dict:
    return {
        "widget": {
            "variant": "full",
            "avatar": {"type": "orb", "color_1": "#6DB035", "color_2": "#F5CABB"},
            "feedback_mode": "during",
            "terms_text": '#### Terms and conditions\n\nBy clicking "Agree," and each time I interact with this AI agent, I consent to the recording, storage, and sharing of my communications with third-party service providers, and as described in the Privacy Policy.\nIf you do not wish to have your conversations recorded, please refrain from using this service.',
            "show_avatar_when_collapsed": True,
        },
        "evaluation": {},
        "auth": {"allowlist": []},
        "overrides": {},
        "call_limits": {"agent_concurrency_limit": -1, "daily_limit": 100000},
        "privacy": {
            "record_voice": record_voice,
            "retention_days": retention_days,
            "delete_transcript_and_pii": True,
            "delete_audio": True,
            "apply_to_existing_conversations": False,
        },
        "data_collection": {},
    }