import speech_recognition as sr

def transcribe_google(file_path):
    audio_data = sr.AudioFile(file_path)

    with audio_data as source:
        audio = sr.Recognizer().record(source)

    result = sr.Recognizer().recognize_google(audio)


    
