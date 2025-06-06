# 🧠 Inquizzy - AI-Powered Quiz App

Inquizzy is a fully interactive, AI-driven quiz application built with **Streamlit** and powered by **Google's Gemini API**. It dynamically generates quiz questions based on selected **domains**, **difficulty levels**, and **question types** (MCQs or True/False), offering users an exam-like experience.

---

## 🚀 Features

### ✨ Quiz Generation
- Uses **Gemini 2.0 Flash API** to generate domain-specific quiz content.
- Supports **multiple domains** like Python, C++, Java, Web Dev, OS, CN, DBMS, Aptitude, and DSA.
- Selectable **difficulty levels**: Easy, Medium, Hard.
- Choose between **MCQs** and **True/False**.

### 🧠 Quiz Interface
- Clean, responsive UI built with Streamlit.
- Live countdown timer with automatic submission when time runs out.
- Side panel for question navigation with color indicators:
  - ✅ Answered
  - 🔲 Not Answered
- Navigate between questions using **Previous** and **Next**.
- Final score revealed only after submission.
- Allows changing answers until quiz is submitted.

### ⚙️ System Design
- Session management for storing quiz state, current question, answers, and timer.
- Persistent answer selection with `st.radio()`.
- API fallback handling and graceful error messages.

### 🎨 UI Enhancements
- Custom gradient-based logo and centered branding.
- Theme-matched navigation and result page styling.

### 📊 Result Page
- Final score summary.
- Correct vs Your answer comparison.
- Return to Home button for retaking quiz.

---

## 📂 Project Structure

```
Inquizzy/
├── app.py                  # Main Streamlit app interface
├── utils/
│   └── fetch_questions.py  # Handles Gemini API and parsing
├── assets/
│   └── logo.png            # App branding logo
├── .env                    # Environment variables (e.g., GEMINI_API_KEY)
└── requirements.txt        # Python dependencies
```

---

## 🛡️ Gemini API Integration
- Uses `google-generativeai` library
- Model: `gemini-2.0-flash`
- Prompts engineered for structured, valid Python lists
- Handles empty, malformed, or unsafe responses

---

## ⚠️ Error Handling
- Invalid question formatting ➜ fallback to local or error message
- API/network failure ➜ visible UI error prompt
- Parsing failure ➜ debug-friendly logs

---

## 📦 Installation

```bash
# Clone the repo
https://github.com/your-username/inquizzy.git
cd inquizzy

# Install dependencies
pip install -r requirements.txt

# Add your Gemini API key
echo GEMINI_API_KEY=your_key_here > .env

# Run the app
streamlit run app.py
```

---

## 🔐 Environment Setup
Create a `.env` file:
```
GEMINI_API_KEY=your_google_gemini_key
```

OR set manually in terminal:
```bash
# Linux/macOS
export GEMINI_API_KEY=your_key

# Windows (CMD)
set GEMINI_API_KEY=your_key
```

---

## 🔗 Deployment
- You can deploy on **Streamlit Cloud**, **Render**, or **Heroku**.
- Make sure to add your `GEMINI_API_KEY` as a secret.

---

## 📌 Future Improvements
- Add leaderboard & user login
- Question analytics dashboard
- PDF export of quiz result
- Admin panel to review generated questions

---

## 🙌 Acknowledgements
- [Google Generative AI](https://ai.google.dev/)
- [Streamlit](https://streamlit.io/)

---

## 📸 Screenshots
> Add your UI screenshots here for settings page, quiz, and results.

---

## 📄 License
MIT License

---

> Made with ❤️ by Deepanshu Pathak
