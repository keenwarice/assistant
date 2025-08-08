import sounddevice as sd
import soundfile as sf
import queue
import json
import time
import numpy as np
from vosk import Model, KaldiRecognizer

model_path = "models/vosk-model-small-en-us-0.15"
SR = 16000
CHANNELS = 1
q = queue.Queue()

def audio_callback(indata,frames, time,status):
    if status:
        print(f"UR CODE IS COOKED!!!! ALERT!! {status}")
    if hear:
        q.put(bytes(indata))

def recognize_from_microphone(on_detect_callback):
    global hear
    hear=True
    model=Model(model_path)
    q.queue.clear()
    recognizer = KaldiRecognizer(model, SR)
    filename=f"recorded_{int(time.time())}.wav"
    audio_frames=[]
    print("speak now you lowly mortal")
    start_time=time.time()
    speech_heard=False
    with sd.RawInputStream(samplerate=SR, blocksize=8000, dtype="int16",channels=1,callback=audio_callback):
        while hear:
            if time.time() - start_time > 5 and not speech_heard: #prevent accidental spying
                print("nvm")
                hear=False
                return
            data=q.get()
            audio_frames.append(data)
            partial=json.loads(recognizer.PartialResult()).get("partial","").strip()
            if partial:
                speech_heard=True
            if recognizer.AcceptWaveform(data):
                result=json.loads(recognizer.Result())
                text= result.get("text","")
                if text:
                    all_audio= b"".join(audio_frames)
                    with sf.SoundFile(filename, mode="x",samplerate=SR, channels=CHANNELS, subtype="PCM_16") as file:
                        file.write(np.frombuffer(all_audio, dtype="int16"))
                    hear=False
                    on_detect_callback(filename, text)
                    print(f"you have said: {text}")
                    return
