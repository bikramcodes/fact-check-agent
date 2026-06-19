from openai import OpenAI
import json
import streamlit as st

openai_key = st.secrets["OPENAI_API_KEY"]

client = OpenAI(api_key=openai_key)

def verify_claim(claim, evidence):

    prompt = f"""
    You are a professional fact checker.

    Claim:
    {claim}

    Evidence:
    {evidence}

    Classify:

    VERIFIED
    INACCURATE
    FALSE

    Return:

    {{
      "status":"",
      "correct_fact":"",
      "explanation":"",
      "confidence":0
    }}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        messages=[{"role":"user","content":prompt}]
    )

    return json.loads(response.choices[0].message.content)
