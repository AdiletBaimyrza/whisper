import speech_recognition as sr

def transcribe_google(file_path):
    audio_data = sr.AudioFile(file_path)

    r = sr.Recognizer()

    with audio_data as source:
        audio = r.record(source)

    result = r.recognize_google(audio, show_all=False)

    print(result)





    
