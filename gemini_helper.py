import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_interview_questions(role, skills):

    prompt = f"""
    Generate 10 interview questions for a {role}.

    Candidate skills:
    {skills}

    Give only questions.
    """
    try:

        response = model.generate_content(prompt)
        return response.text

    except Exception as e:

        print(f"Gemini Error: {e}")

def generate_skill_gap_analysis(role, detected_skills):

    prompt = f"""
    I am preparing for a {role} role.

    My current skills are:
    {detected_skills}

    Analyze my profile and provide:

    1. Strengths
    2. Missing skills
    3. Suggestions for improvement
    4. Recommended projects

    Format the response nicely.
    """

    response = model.generate_content(prompt)

    return response.text

def generate_resume_suggestions(resume_text):

    prompt = f"""
    Analyze the following resume:

    {resume_text}

    Provide:

    1. Strengths
    2. Weaknesses
    3. Suggestions for improvement
    4. Certifications to pursue
    5. Project ideas

    Format the response properly.
    """

    response = model.generate_content(prompt)

    return response.text

def generate_ats_feedback(role, skills, resume_text):

    prompt = f"""
    I am applying for a {role} role.

    My skills are:
    {skills}

    Resume content:
    {resume_text}

    Give ATS feedback.

    Include:
    1. Resume strengths
    2. Missing keywords
    3. Areas to improve
    4. ATS friendliness score out of 10

    Format properly.
    """

    response = model.generate_content(prompt)

    return response.text