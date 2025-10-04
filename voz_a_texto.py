import speech_recognition as sr

def reconocer_voz():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ajustando al ruido ambiental, espera 2 segundos...")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Por favor, hable ahora...")
        try:
            # Escucha hasta 15 segundos de frase
            audio = recognizer.listen(source, phrase_time_limit=15)
        except sr.WaitTimeoutError:
            print("No detecté tu voz a tiempo, intenta de nuevo")
            return
    
    try:
        texto = recognizer.recognize_google(audio, language="es-MX")
        print(f"Has dicho: {texto}")
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
    except sr.RequestError as e:
        print(f"Error al solicitar resultados; {e}")

if __name__ == "__main__":
    reconocer_voz()


