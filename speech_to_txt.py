import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()
    mic_index = 23  # Your working mic index

    try:
        with sr.Microphone(device_index=mic_index) as source:
            print("🎙️ Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)

            print("🗣️ Speak now...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

            print("🔍 Recognizing speech...")
            text = recognizer.recognize_google(audio)
            print("✅ You said:", text)

    except sr.WaitTimeoutError:
        print("⏳ Timeout: No speech detected.")
    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
    except sr.RequestError as e:
        print(f"⚠️ API Error: {e}")
    except Exception as e:
        print(f"🚫 Unexpected Error: {e}")

speech_to_text()
