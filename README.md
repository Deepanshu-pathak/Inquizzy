# 🧠 Inquizzy - Quiz App

**No login. No signup. Just pure knowledge testing.** <br>
Inquizzy is a AI-powered quiz platform crafted for curious minds and fast learners. Built to simplify knowledge checks, it offers an effortless and focused way to test yourself across technical domains.


---
## 🌐 Live Demo
Try out the app here: <br>
👉 https://inquizzy.streamlit.app

---

## 🚀 Features

#### ✨ Quiz Generation
- Uses **Gemini API** to generate domain-specific quiz content.
- Supports **multiple domains** like Python, C++, Java, Web Dev, OS, Aptitude, DSA etc.
- Selectable **difficulty levels**: Easy, Medium, Hard.
- Choose between **MCQs** and **True/False**.

#### 🧠 Quiz Interface
- Clean, responsive UI built with Streamlit.
- Side panel for question navigation with indicators:
  - ✅ Answered
  - 🔲 Not Answered
- Navigate between questions using **Prev** and **Next** buttons.
- Final score revealed after submission.

#### 📊 Result Page
- Final score summary.
- Correct vs Your answer comparison.
- Return to Home button for retaking quiz.

---

## 🛡️ Gemini API Integration
- Uses `google-genai` library
- Model: `gemini-2.0-flash`
- Prompts engineered for structured, valid Python lists
- Handles empty, malformed, or unsafe responses

---

## 🙌 Acknowledgements
- [Google Generative AI](https://ai.google.dev/)
- [Streamlit](https://streamlit.io/)
