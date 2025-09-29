import speech_recognition as sr

def listar_microfonos():
    print("Micrófonos disponibles:")
    mic_list = sr.Microphone.list_microphone_names()
    for i, mic in enumerate(mic_list):
        print(f"{i}: {mic}")
    return mic_list

def reconocer_voz(device_index=None):
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=device_index) as source:
        print("Habla algo...")
        audio = recognizer.listen(source)
        try:
            texto = recognizer.recognize_google(audio, language="es-ES")
            print("Has dicho: " + texto)
        except sr.UnknownValueError:
            print("No se pudo entender el audio")
        except sr.RequestError as e:
            print(f"Error al solicitar resultados; {e}")

if __name__ == "__main__":
    mic_list = listar_microfonos()
    indice = input("Ingresa el número del micrófono que quieres usar: ")
    try:
        indice = int(indice)
        if 0 <= indice < len(mic_list):
            reconocer_voz(device_index=indice)
        else:
            print("Número de micrófono no válido.")
    except ValueError:
        print("Debes ingresar un número válido.")
