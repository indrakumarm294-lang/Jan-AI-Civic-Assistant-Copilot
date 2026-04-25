import streamlit as st
from utils.rag import get_answer
from utils.translate import detect_language, translate_to_english, translate_to_user_lang
from utils.translate import normalize_currency
from utils.speech import text_to_speech

# =========================
# PAGE CONFIG (MUST BE FIRST)
# =========================
st.set_page_config(page_title="Jan AI Civic Copilot", layout="centered")

# =========================
# CSS (MODERN UI)
# =========================
st.markdown("""
<style>

/* App background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f172a, #1e1b4b);
    color: white;
}

/* Glass card */
.glass-card {
    background: rgba(255, 255, 255, 0.07);
    border-radius: 18px;
    padding: 18px;
    margin: 12px 0;
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
    transition: 0.3s ease;
}

.glass-card:hover {
    transform: translateY(-4px);
}

/* Title */
h1 {
    text-align: center;
    font-size: 34px;
    font-weight: 800;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("<h1>🇮🇳 Civic Copilot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Smart AI for Government Schemes 🚀</p>", unsafe_allow_html=True)

# =========================
# SESSION STATE
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================
# SIDEBAR FILTER
# =========================
category = st.selectbox(
    "Select category",
    ["All", "farmer", "health", "business", "jobs", "student"]
)

selected_category = None if category == "All" else category

# =========================
# CHAT HISTORY DISPLAY
# =========================
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"], unsafe_allow_html=True)

# =========================
# USER INPUT
# =========================
user_input = st.chat_input("Ask about government schemes...")

if user_input:

    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    # Detect language
    user_lang = detect_language(user_input)

    # Translate query to English
    query_en = translate_to_english(user_input)

    # Get RAG response
    results = get_answer(query_en, selected_category)

    if results:

        for res in results:

            # normalize ₹
            clean_details = normalize_currency(res["details"])
            clean_eligibility = normalize_currency(res["eligibility"])

            # raw text block (ONLY TEXT, NO HTML)
            text_block = f"""
            Scheme: {res['name']}
            Details: {clean_details}
            Eligibility: {clean_eligibility}
            """

            # translate ONLY text
            translated_text = translate_to_user_lang(text_block, user_lang)

            # build UI AFTER translation (NO double translation)
            card = f"""
            <div class="glass-card">
                <h3>📌 {res['name']}</h3>
                <p>{translated_text}</p>
            </div>
            """

            # show assistant message
            with st.chat_message("assistant"):
                st.markdown(card, unsafe_allow_html=True)

            # save chat history
            st.session_state.messages.append({
                "role": "assistant",
                "content": card
            })

            # =========================
            # VOICE OUTPUT (FIXED)
            # =========================
            try:
                speech_text = f"{res['name']}. {res['details']}. Eligibility: {res['eligibility']}"

                speech_text = normalize_currency(speech_text)

                translated_speech = translate_to_user_lang(speech_text, user_lang)

                audio = text_to_speech(translated_speech, user_lang)
                st.audio(audio)

            except:
                pass

    else:
        msg = "Sorry, no matching schemes found."
        translated = translate_to_user_lang(msg, user_lang)

        with st.chat_message("assistant"):
            st.warning(translated)

        st.session_state.messages.append({
            "role": "assistant",
            "content": translated
        })