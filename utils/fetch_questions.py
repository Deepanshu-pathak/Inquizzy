from utils.gemini_client import generate_questions

def fetch_questions(category="Python", difficulty="medium", qtype="mcq", limit=5):
    questions = generate_questions(category, difficulty, qtype, limit)
    if questions:
        return questions
