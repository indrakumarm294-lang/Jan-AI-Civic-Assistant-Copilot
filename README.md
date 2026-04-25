# Jan-AI-Civic-Assistant-Copilot
“JanAI Civic Assistant is a multilingual AI system that helps users find and understand government schemes. It provides personalized, accurate guidance using NLP, RAG, and LLM, allowing users to access eligibility, benefits, and details easily in their own language.”

# 🇮🇳 JanAI – Multilingual Civic Assistant Copilot

## 📌 Overview
JanAI is an AI-powered multilingual civic assistant that helps users easily understand and access government schemes. It provides personalized eligibility checking, accurate information, and simple explanations in regional languages.

---

## ❗ Problem Statement
Many citizens face challenges in:
- Understanding government schemes
- Language barriers (English-heavy platforms)
- Identifying eligibility
- Avoiding misinformation

---

## 💡 Solution
JanAI solves this by:
- Providing **multilingual support** (English, Hindi, Kannada,etc)
- Offering **personalized eligibility checks**
- Using **RAG (Retrieval-Augmented Generation)** to ensure accuracy
- Giving **simple and easy-to-understand explanations**

---

## 🚀 Features
- 🌍 Multilingual interaction
- 🧠 Personalized eligibility engine
- 🔍 Scheme retrieval system
- 🤖 AI-generated responses (LLM)
- 🎙️voice assistant integration
- 📱 Mobile-friendly web app
- 🧾 Simple explanation mode

---

## 🧠 How It Works (RAG Architecture)

User Query → Retrieve Scheme Data → AI Generates Response → Output

- Retrieves verified data from database
- AI generates answers based  on ONLY retrieved data
- Prevents hallucination and misinformation

---

## 🛠️ Tech Stack
- Python
- Streamlit
- openai whisper
- Deep Translator
- JSON (Database)

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
streamlit run app.py
