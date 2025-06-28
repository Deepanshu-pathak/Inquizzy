from google import genai
import ast
import os
import streamlit as st

GEMINI_API_KEY= os.getenv("GEMINI_API_KEY")
client =genai.Client(api_key=GEMINI_API_KEY)

def generate_questions(domain, difficulty, q_type="mcq", limit=5):
    if q_type.lower() == "true/false":
        prompt = (
            "You are a quiz generator. Generate exactly {} True/False questions on the topic of '{}' with {} difficulty.\n"
            "Each question should be a dictionary in a list with the following structure:\n"
            "- 'question': string (the question text)\n"
            "- 'options': list of two strings: ['True', 'False']\n"
            "- 'correct_answer': string (either 'True' or 'False')\n"
            "Return the response as valid Python list of dictionaries. Do not include explanations or markdown."
        ).format(limit, domain, difficulty)
    else:
        prompt = (
            "You are a quiz generator. Generate exactly {} unique MCQ questions on the topic of '{}' with {} difficulty.\n"
            "Each question should be a dictionary in a list with the following structure:\n"
            "- 'question': string (the question text)\n"
            "- 'options': list of 4 strings (plausible and unique answer choices)\n"
            "- 'correct_answer': string (one of the options)\n"
            "Return the response as valid Python list of dictionaries. Do not include explanations or markdown."
        ).format(limit, domain, difficulty)

    try:
        with st.spinner("Generating quiz questions... please wait"):
            response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
            questions = ast.literal_eval(response.text.strip().strip('```python').strip('```').strip())
            return questions        

    except Exception as e:
        print("Gemini generation failed:", e)
        return []
