# import google.genai as genai
from google import genai
import json
import os
from dotenv import load_dotenv
from .models import AILog


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.Client(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-flash')


def fallback_task(text):
    AILog.objects.create(
        input_text=text,
        error_message="AI Parsing failed"
    )

    return {
        'title': text,
        'due_date': None,
        'priority': "Medium",
        'category': "Other"
    }


def parse_task(text: str) -> dict:
    prompt = f"""
You are a task extraction assistant.

Extract task information from the text below.
Return ONLY valid JSON (no markdown, no explanation).


Allowed Categories:
("Work", "Study", "Health", "Personal", "Other")

JSON fields:
- title(string)
- due_date (YYYY-MM-DD HH:MM or null)
- priority(High, Medium, Low)
- category (from allowed list)

Text:
{text}

"""

    response = model.generate_content(prompt)

    try:
        data = json.loads(response.text)

        if data['category'] not in ["Work", "Study", "Health", "Personal", "Other"]:
            data['category'] = "Other"

        return data

    except Exception:
        return fallback_task(text)
