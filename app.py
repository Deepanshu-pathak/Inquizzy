import streamlit as st
from utils.fetch_questions import fetch_questions
import time
from PIL import Image

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'settings'
if 'questions' not in st.session_state:
    st.session_state.questions = []
if 'quiz_settings' not in st.session_state:
    st.session_state.quiz_settings = {}
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'total_time' not in st.session_state:
    st.session_state.total_time = 0
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'current_q' not in st.session_state:
    st.session_state.current_q = 0

logo = Image.open("assets/Inquizzy LOGO.png")
st.set_page_config(page_title='Inquizzy',page_icon=logo)


# HEADER
st.markdown("""
    <style>
        .main-title { font-size: 40px; font-weight: 700; color: #ff4b4b; text-align: center; }
        .question-card { background-color: #f9f9f9; padding: 20px; border-radius: 10px; border: 1px solid #eee; }
        .quiz-controls { text-align: center; padding-top: 10px; }
    </style>
    <h1 class='main-title'>Inquizzy</h1>
""", unsafe_allow_html=True)


# SETTINGS PAGE
if st.session_state.page == 'settings':
    with st.container():
        st.subheader("🎯 Quiz Setup")
        domain = st.selectbox("📚 Select Domain:", [
            "Python", "C++", "Java", "Web Development", "DSA", "Aptitude","Science", "DBMS", "Operating Systems", "Computer Networks"
        ])
        difficulty = st.selectbox("🚦 Select Difficulty:", ["Easy", "Medium", "Hard"])
        q_type = st.selectbox("📝 Question Type:", ["MCQ", "True/False"])
        num_questions = st.slider("🔢 Number of Questions:", 5, 20, 5)

        if st.button("🚀 Start Quiz"):
            st.session_state.quiz_settings = {
                "domain": domain,
                "difficulty": difficulty,
                "q_type": q_type,
                "num_questions": num_questions
            }
            questions = fetch_questions(domain, difficulty, q_type, num_questions)
            
            st.session_state.questions = questions 
            st.session_state.answers = {}
            st.session_state.current_q = 0
            st.session_state.page = 'quiz'
            st.session_state.submitted = False
            st.session_state.total_time = num_questions * 30  # 30 seconds per question
            st.session_state.start_time = time.time()
            st.rerun()

# QUIZ PAGE
elif st.session_state.page == 'quiz':
    questions = st.session_state.questions
    total_q = len(questions)
    q_idx = min(st.session_state.current_q, total_q - 1)
    current_q = questions[q_idx]
    st.session_state.current_q = q_idx

    # TIMER
    elapsed = int(time.time() - st.session_state.start_time)
    remaining = max(0, st.session_state.total_time - elapsed)
    mins, secs = divmod(remaining, 60)
    st.sidebar.title(f"⏳ Time Left: {mins:02d}:{secs:02d}")    

    if remaining == 0 and not st.session_state.submitted:
        st.session_state.page = 'result'
        st.rerun()


    # Question palette
    st.sidebar.markdown("### 🔢 Navigate Questions")
    for i in range(total_q):          
        btn_label = f"{i+1}"
        style = "✅" if i in st.session_state.answers else "🔲"
        if st.sidebar.button(f"{style} Q{i+1}"):
            st.session_state.current_q = i
            st.rerun()

    # Display current question
    st.markdown(f"### Question {q_idx + 1} of {total_q}")
    with st.container():
        st.write(current_q['question'])

        selected_index = 0
        if q_idx in st.session_state.answers:
            try:
                selected_index = current_q['options'].index(st.session_state.answers[q_idx])
            except ValueError:
                selected_index = -1

        selected = st.radio("Select an answer:", current_q['options'], index=selected_index, key=f"q_{q_idx}")
        st.session_state.answers[q_idx] = selected
        st.markdown("</div>", unsafe_allow_html=True)

    # Navigation buttons
    col1, col2 = st.columns([1, 2])
    with col1:
        if q_idx > 0:
            if st.button("⬅️ Previous"):
                st.session_state.current_q -= 1
                st.rerun()

    with col2:
        if q_idx < total_q - 1:
            if st.button("Next ➡️"):
                st.session_state.current_q += 1
                st.rerun()

    # Submit button only on last question
    if q_idx == total_q - 1:
        if st.button("✅ Submit Quiz"):
            st.session_state.page = 'result'
            st.rerun()

# RESULT PAGE
elif st.session_state.page == 'result':
    if st.button("Return to Home"):
        st.session_state.page = 'settings'
        st.rerun()

    st.title("🎉 Quiz Completed!")
    score = 0
    for idx, q in enumerate(st.session_state.questions):
        correct = q['correct_answer']
        given = st.session_state.answers.get(idx)
        if given == correct:
            score += 1
    total = len(st.session_state.questions)
    st.markdown(f"### Your Score: **{score} / {total}**")
    st.markdown("✅ = Correct, ❌ = Incorrect")
    for idx, q in enumerate(st.session_state.questions):
        correct = q['correct_answer']
        given = st.session_state.answers.get(idx, "Not Answered")
        status = "✅" if given == correct else "❌"
        st.markdown(f"**Q{idx+1}:** {q['question']}")
        st.markdown(f"- Your Answer: {given}")
        st.markdown(f"- Correct Answer: {correct} {status}")
        st.markdown("---")
