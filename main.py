import os
from audio.wake_word import detect_wake_word
from stt.transcriber import recognize_from_microphone
from ai.recognition import recognize_user
from ai.ai_response import respond
import pyttsx3
engine = pyttsx3.init() 
engine.setProperty('rate', 175)
engine.setProperty('volume',1.0) 
engine.setProperty('voice', engine.getProperty('voices')[14].id) # CHANGE THIS TO THE BEST ONE FOR YOUR OS
def start():
    while True:
        detect_wake_word(after)

def after():
    print("WAKE WORD DETECTED")
    recognize_from_microphone(send_phrase)

def send_phrase(filename, phrase):
    name, score= recognize_user(filename)
    print(name+":"+phrase)
    try:
        os.remove(filename)
        print("privacy secured! "+filename+" is gone!")
    except Exception as e:
        print("PRIVACY MAY BE IN RISK: ",e)
    response=respond(phrase,name)
    print(response)
    engine.say(response)
    engine.runAndWait()
    engine.stop()

if __name__ == "__main__":
    start()
