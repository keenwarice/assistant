import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
from ai.recognition import add_user
from time import sleep

def rec_sound(filename="recording.wav", duration=5, fs=16000):
    print("recording will start in 3 seconds and will last 5 seconds. speak immediatley")
    sleep(3)
    print("start speaking.")
    audio= sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype=np.int16)
    sd.wait()
    write(filename, fs, audio)
    if input("recording saved. train? Y/N").lower() == "y":
        add_user(input("what is your name?").lower(),filename)
    else:
        print("cancelled.")

if __name__ == "__main__":
    rec_sound()
