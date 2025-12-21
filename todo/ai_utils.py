# todo/ai_utils.py
import os
import json
from google import genai
from .models import AILog


def get_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set")

    return genai.Client(api_key=api_key)


def fallback_task(text):
    AILog.objects.create(
        input_text=text,
        error_message="AI Parsing failed"
    )

    return {
        "title": text,
        "due_date": None,
        "priority": "Medium",
        "category": "Other",
    }


def parse_task(text: str) -> dict:
    prompt = f"""
You are a task extraction assistant.

Extract task information from the text below.
Return ONLY valid JSON (no markdown, no explanation).

Allowed Categories:
("Work", "Study", "Health", "Personal", "Other")

JSON fields:
- title (string)
- due_date (YYYY-MM-DD HH:MM or null)
- priority (High, Medium, Low)
- category (from allowed list)

Text:
{text}
"""

    try:
        client = get_client()

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        data = json.loads(response.text)

        if data.get("category") not in [
            "Work", "Study", "Health", "Personal", "Other"
        ]:
            data["category"] = "Other"

        return data

    except Exception as e:
        return fallback_task(text)
