import speech_recognition as sr

def reconocer_voz():
    recognizer = sr.Recognizer()
    # Micrófono fijo: cambiar 1 por el índice correcto de tu micrófono
    mic_index = 1

    with sr.Microphone(device_index=mic_index) as source:
        print("Habla algo...")
        audio = recognizer.listen(source)
        try:
            texto = recognizer.recognize_google(audio, language="es-ES")
            print("Has dicho:", texto)
        except sr.UnknownValueError:
            print("No se entendió el audio")
        except sr.RequestError as e:
            print(f"Error con el servicio de Google: {e}")

reconocer_voz()
# Asegúrate de tener instalado el paquete speech_recognition:
