import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_gemini(df, question):
    prompt = f"""
You are an expert Data Analyst.

Dataset Columns:
{list(df.columns)}

Dataset Preview:
{df.head(20).to_string()}

Dataset Statistics:
{df.describe(include='all').to_string()}

User Question:
{question}

Answer in simple English.
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Gemini Error: {e}"