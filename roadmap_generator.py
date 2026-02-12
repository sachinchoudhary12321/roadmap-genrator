import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/openai/",api_key=os.getenv("OPENAI_API_KEY"))

def generate_roadmap(skill, level, goal):

    prompt = f"""
    You are a professional career mentor.

    Generate a structured learning roadmap for:
    Skill: {skill}
    Level: {level}
    Goal: {goal}

    Include:
    - Timeline (weeks/months)
    - Topics step-by-step
    - Projects
    - Tools
    - Free resources
    - Interview preparation steps
    """

    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "system", "content": "You are a career mentorship AI."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
