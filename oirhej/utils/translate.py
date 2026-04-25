from langdetect import detect
from deep_translator import GoogleTranslator
import time

# Supported Indian languages
SUPPORTED_LANGS = {
    "hi": "hindi",
    "kn": "kannada",
    "ta": "tamil",
    "te": "telugu",
    "en": "english"
}

def detect_language(text):
    try:
        lang = detect(text)
        if lang in SUPPORTED_LANGS:
            return lang
        return "en"
    except:
        return "en"

# 🔁 Safe translator with retry
def safe_translate(text, source, target):
    for _ in range(2):  # retry 2 times
        try:
            translator = GoogleTranslator(source=source, target=target)
            return translator.translate(text)
        except Exception:
            time.sleep(0.3)  # small delay before retry
    return text  # fallback

def translate_to_english(text):
    return safe_translate(text, 'auto', 'en')

def translate_to_user_lang(text, lang):
    if lang == "en":
        return text
    return safe_translate(text, 'en', lang)
def normalize_currency(text):
    return text.replace("₹", "INR ").replace("Rs.", "INR ")