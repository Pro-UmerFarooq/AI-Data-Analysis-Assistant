# ai_helper.py

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def get_client():
    """
    Create Groq client using API Key.
    """
    print("API KEY:", os.getenv("GEMINI_API_KEY"))
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return None

    return Groq(api_key=api_key)


def generate_ai_explanation(dataset_summary):
    """
    Sends dataset summary to Groq AI
    and returns an easy explanation.
    """

    client = get_client()

    if client is None:
        return "❌ GROQ_API_KEY not found. Please add it."

    prompt = f"""
You are an expert Data Analyst.

Explain the following dataset analysis in very simple English.

Dataset Summary:

{dataset_summary}

Requirements:

1. Explain in simple English.
2. Mention important findings.
3. Mention unusual patterns if any.
4. Keep the explanation under 150 words.
"""

    try:

        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.3,
            max_tokens=250

        )

        return response.choices[0].message.content

    except Exception as e:

        return f"AI Error : {e}"