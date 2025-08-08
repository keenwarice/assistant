# some borrowed from the other file
import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer


model_path = "models/vosk-model-small-en-us-0.15"
SR = 16000
q = queue.Queue()

def audio_callback(indata,frames, time,status):
    if status:
        print(f"UR CODE IS COOKED!!!! ALERT!! {status}")
    q.put(bytes(indata))

def detect_wake_word(on_detect_callback):
    model=Model(model_path)
    wake_words= ["sirius", "serious", "seriously"] # just in case
    recognizer = KaldiRecognizer(model, SR)
    q.queue.clear()
    print(wake_words)
    last_detected=""
    with sd.RawInputStream(samplerate=SR, blocksize= 8000, dtype="int16", channels=1,callback=audio_callback):
        while True:
            data= q.get()
            recognizer.AcceptWaveform(data)
            partial_result=recognizer.PartialResult()
            partial_text=json.loads(partial_result).get("partial", "").strip().lower()
            if partial_text:
                last_word=partial_text.split()[-1]
                if last_word in wake_words and last_word != last_detected:
                    on_detect_callback()
                    last_detected = last_word
                    return
                elif last_word != last_detected:
                    last_detected=""
