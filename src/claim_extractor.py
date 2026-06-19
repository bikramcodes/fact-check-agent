from openai import OpenAI
import json
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_claims(text):

    prompt = f"""
    Extract all factual claims.

    Focus on:
    - Statistics
    - Dates
    - Percentages
    - Financial figures
    - Technical metrics

    Return JSON array only.

    Text:
    {text[:15000]}
    """

    response = client.chat.completions.create(
        
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return json.loads(response.choices[0].message.content)