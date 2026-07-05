import json

from models.intent import VideoIntent
from models.state import PipelineState
from services.gemini_service import client


def intent_parser(state: PipelineState) -> PipelineState:
    """
    Intent Parser Agent

    Parses the user's prompt into a structured VideoIntent
    using Gemini.
    """

    print("=" * 60)
    print("🧠 Intent Parser Agent Started")
    print("=" * 60)

    prompt = f"""
You are an AI video planning assistant.

Extract the user's intent and return ONLY valid JSON.

Required format:

{{
    "video_style": "",
    "mood": "",
    "pacing": "",
    "transition": "",
    "duration": 30,
    "music_style": ""
}}

User Prompt:
{state.user_prompt}
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        text = (
            response.text
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        data = json.loads(text)

        state.video_intent = VideoIntent(**data)

        print("✅ Intent Parsed Successfully")

    except Exception as e:

        print("⚠️ Gemini unavailable. Using fallback intent.")
        print(e)

        state.video_intent = VideoIntent(
            video_style="Cinematic",
            mood="Emotional",
            pacing="Slow",
            transition="Fade",
            duration=30,
            music_style="Instrumental"
        )

    print(state.video_intent)

    state.status = "intent_parsed"

    return state