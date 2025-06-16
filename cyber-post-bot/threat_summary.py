import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_cyber_threat_summary():
    prompt = (
        "Summarize the top 3 most important cybersecurity threats from the last 7 days. "
        "Include CVEs, threat actors, or breaches. Use plain language."
    )
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )
    return response.choices[0].message['content'].strip()
