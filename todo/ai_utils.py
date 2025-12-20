import google.generativeai as genai
import json
import os
from dotenv import load_dotenv


load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash')


def parse_task(text: str) -> dict:
    prompt = f"""
You are a task extraction assistant.

Extract task information from the text below.
Return ONLY valid JSON (no markdown, no explanation).

JSON fields:
- title(string)
- due_date (YYYY-MM-DD HH:MM or null)
- priority(High, Medium, Low)

Text:
{text}

"""

    response = model.generate_content(prompt)

    try:
        return json.loads(response.text)
    except json.JSONDecodeError:
        return {
            'title': text,
            'due_date': None,
            'priority': "Medium"
        }
