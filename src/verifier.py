from openai import OpenAI
import json
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
        messages=[{"role":"user","content":prompt}]
    )

    return json.loads(response.choices[0].message.content)
