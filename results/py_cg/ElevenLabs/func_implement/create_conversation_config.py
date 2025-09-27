# file: /Users/xue/workspace/mcp_project/mcp_server_pyrepos/elevenlabs/elevenlabs_mcp/convai.py
# module: elevenlabs_mcp.convai
# qname: elevenlabs_mcp.convai.create_conversation_config
# lines: 1-59
def create_conversation_config(
    language: str,
    system_prompt: str,
    llm: str,
    first_message: str | None,
    temperature: float,
    max_tokens: int | None,
    asr_quality: str,
    voice_id: str | None,
    model_id: str,
    optimize_streaming_latency: int,
    stability: float,
    similarity_boost: float,
    turn_timeout: int,
    max_duration_seconds: int,
) -> dict:
    return {
        "agent": {
            "language": language,
            "prompt": {
                "prompt": system_prompt,
                "llm": llm,
                "tools": [{"type": "system", "name": "end_call", "description": ""}],
                "knowledge_base": [],
                "temperature": temperature,
                **({"max_tokens": max_tokens} if max_tokens else {}),
            },
            **({"first_message": first_message} if first_message else {}),
            "dynamic_variables": {"dynamic_variable_placeholders": {}},
        },
        "asr": {
            "quality": asr_quality,
            "provider": "elevenlabs",
            "user_input_audio_format": "pcm_16000",
            "keywords": [],
        },
        "tts": {
            **({"voice_id": voice_id} if voice_id else {}),
            "model_id": model_id,
            "agent_output_audio_format": "pcm_16000",
            "optimize_streaming_latency": optimize_streaming_latency,
            "stability": stability,
            "similarity_boost": similarity_boost,
        },
        "turn": {"turn_timeout": turn_timeout},
        "conversation": {
            "max_duration_seconds": max_duration_seconds,
            "client_events": [
                "audio",
                "interruption",
                "user_transcript",
                "agent_response",
                "agent_response_correction",
            ],
        },
        "language_presets": {},
        "is_blocked_ivc": False,
        "is_blocked_non_ivc": False,
    }