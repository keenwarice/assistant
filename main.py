import os
from audio.wake_word import detect_wake_word
from stt.transcriber import recognize_from_microphone
from ai.recognition import recognize_user
from ai.ai_response import respond

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
        print("PRIVACY MAY BE IN RISK: "+e)
    print(respond(phrase,name))
    
if __name__ == "__main__":
    detect_wake_word(after) #had to do this because python didnt let me run it
