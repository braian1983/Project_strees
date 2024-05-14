import SpeechRecognition as sr # type: ignore
import time

def listen_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga algo...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='pt-BR')
        print("Você disse: " + text)
        return text
    except:
        print("Não foi possível reconhecer a fala.")
        return None

def main():
    while True:
        voice_text = listen_voice()
        if voice_text is not None:
            print(f"Você disse: {voice_text}")

def main():
    while True:
        voice_text = listen_voice()
        if voice_text is not None:
            print(f"Você disse: {voice_text}")
        time.sleep(1)   
