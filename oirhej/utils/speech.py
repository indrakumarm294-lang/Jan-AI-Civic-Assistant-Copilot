import edge_tts
import asyncio
import uuid

async def speak(text, voice, file):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(file)

def text_to_speech(text, lang="en"):
    file = f"output_{uuid.uuid4().hex}.mp3"

    VOICES = {
        "en": "en-IN-PrabhatNeural",
        "hi": "hi-IN-SwaraNeural",
        "ta": "ta-IN-PallaviNeural",
        "te": "te-IN-ShrutiNeural",
        "kn": "kn-IN-SapnaNeural"
    }

    voice = VOICES.get(lang, VOICES["en"])

    asyncio.run(speak(text, voice, file))

    return file