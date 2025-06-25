from audio.wake_word import detect_wake_word
from stt.transcriber import recognize_from_microphone


def after():
    print("WAKE WORD DETECTED")
    recognize_from_microphone(send_phrase)

def send_phrase(filename, phrase):
    print("phrase recieved")
    print(phrase)

if __name__ == "__main__":
    detect_wake_word(after) #had to do this because python didnt let me run it
