import recording
import transcribing

recording.record_to_file("output.wav")
transcribing.transcribe_google("output.wav")