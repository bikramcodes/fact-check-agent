from openai import OpenAI
import json
import streamlit as st

openai_key = st.secrets["OPENAI_API_KEY"]

client = OpenAI(api_key=openai_key)

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
        response_format={"type": "json_object"},
        messages=[{"role":"user","content":prompt}]
    )

    return json.loads(response.choices[0].message.content)
