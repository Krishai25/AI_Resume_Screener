from groq import Groq
import json
import os
from dotenv import load_dotenv

load_dotenv()

def screen_resume(resume_text, job_description):

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    prompt = f"""
You are an expert HR recruiter and resume analyst.

I will give you a RESUME and a JOB DESCRIPTION.

Your job is to analyze them and return:
1. A match score from 0 to 100
2. A list of matched skills
3. A list of missing skills
4. A short summary of 2-3 sentences

Reply ONLY in this exact JSON format, nothing else:
{{
  "score": <number>,
  "matched_skills": ["skill1", "skill2"],
  "missing_skills": ["skill1", "skill2"],
  "summary": "your feedback here"
}}

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    response_text = response.choices[0].message.content
    result = json.loads(response_text)
    return result