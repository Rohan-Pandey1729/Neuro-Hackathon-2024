from flask import Flask
import matplotlib.pyplot as plt
import numpy as np
from dotenv import load_dotenv
import random
import soundfile as sf
import sounddevice as sd

from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets
from brainflow import ml_model
from brainflow.ml_model import *

app = Flask(__name__)

@app.route("/")
def questions():
    genres = [
        "blues", "classical", "country", "disco", "hiphop",
        "jazz", "metal", "pop", "reggae", "rock"
    ]
    pace_preference = input("Do you prefer fast-paced music or slow-paced music? (Type 'fast' or 'slow'): ")
    instrumental_preference = input("Do you prefer instrumental music or songs with lyrics? (Type 'instrumental' or 'lyrics'): ")
    beat_preference = input("Do you prefer music with heavy beats or more melodic tunes? (Type 'heavy beats' or 'melodic'): ")
    energy_preference = input("Would you rather listen to music that energizes you or music that helps you relax? (Type 'energizing' or 'relaxing'): ")
    genre_mappings = {
        ('fast', 'heavy beats', 'instrumental', 'energizing'): {"disco", "hiphop", "metal"},
        ('fast', 'heavy beats', 'instrumental', 'relaxing'): {"pop", "jazz", "classical"},
        ('fast', 'melodic', 'lyrics', 'energizing'): {"disco", "pop", "hiphop"},
        ('fast', 'melodic', 'lyrics', 'relaxing'): {"pop", "classical", "jazz"},
        ('slow', 'heavy beats', 'instrumental', 'energizing'): {"reggae", "jazz", "metal"},
        ('slow', 'heavy beats', 'instrumental', 'relaxing'): {"classical", "jazz", "reggae"},
        ('slow', 'melodic', 'lyrics', 'energizing'): {"reggae", "hiphop", "jazz"},
        ('slow', 'melodic', 'lyrics', 'relaxing'): {"reggae", "classical", "jazz"}
    }
    genre_count = {genre: 0 for genre in genres}
    for preference_set, genre_set in genre_mappings.items():
        if (pace_preference, beat_preference, instrumental_preference, energy_preference) == preference_set:
            for genre in genre_set:
                genre_count[genre] += 1
    sorted_genres = sorted(genre_count.keys(), key=lambda x: genre_count[x], reverse=True)
    top_three_genres = set(sorted_genres[:3])
    return top_three_genres

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)