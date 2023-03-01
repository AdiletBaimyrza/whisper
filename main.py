import recording
import transcribing

recording.record_to_file("output.wav")
transcribing.transcribe_whisper("base", "output.wav")