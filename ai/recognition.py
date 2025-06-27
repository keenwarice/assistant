import os
import numpy as np
import pickle
from resemblyzer import VoiceEncoder, preprocess_wav

embeddings_file= "ai/voice_profiles.pkl"
encoder= VoiceEncoder()

if os.path.exists(embeddings_file):
    with open(embeddings_file, "rb") as f:
        voice_db=pickle.load(f)
else:
    voice_db={}

#planning to make this a feature that the assistant can call to easily add people
def add_user(name, filename):
    print("training for "+name)
    wav= preprocess_wav(filename)
    embedding= encoder.embed_utterance(wav)
    voice_db[name] = embedding

    with open(embeddings_file, "wb") as f:
        pickle.dump(voice_db, f)
    print("saved "+name)

def recognize_user(filename):
    if not voice_db:
        print("cant find any voices. run trainvoice.py to add your voice")
        return "unrecognized voice", None

    print("recognizing from "+ filename)
    wav=preprocess_wav(filename)
    embedding=encoder.embed_utterance(wav)
    best_match=None
    best_score= -1
    for name, ref_embedding in voice_db.items():
        score= np.dot(embedding, ref_embedding)
        print(f"similarity to {name} is {score:.3f}")
        if score > best_score:
            best_score=score
            best_match=name
    return best_match, best_score
