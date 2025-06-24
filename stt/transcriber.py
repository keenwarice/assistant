import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer

model_path = "models/vosk-model-small-en-us-0.15"
SR = 16000
q = queue.Queue() # i was a bit confused with the spelling, skull

def audio_callback(indata,frames, time,status):
    if status:
        print(f"UR CODE IS COOKED!!!! ALERT!! {status}")
    q.put(bytes(indata))

def recognize_from_microphone():
    model=Model(model_path)
    recognizer = KaldiRecognizer(model, SR)

    print("speak now you lowly mortal")
    with sd.RawInputStream(samplerate=SR, blocksize=8000, dtype="int16",channels=1,callback=audio_callback):
        while True:
            data=q.get()
            if recognizer.AcceptWaveform(data):
                result=json.loads(recognizer.Result())
                text= result.get("text","")
                if text:
                    print(f"you have said: {text}")
