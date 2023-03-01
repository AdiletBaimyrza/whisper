import whisper

def transcribe_whisper(model, file_path):
    model = whisper.load_model(model)
    result = model.transcribe(file_path)
    print(result["text"])