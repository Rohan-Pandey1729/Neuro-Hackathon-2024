import random
import soundfile as sf
import sounddevice as sd
import os

def get_random_clip_file(genre: str) -> str:
    i = random.randint(0, 9)
    return os.path.join("genre_clip_data", genre, f'{genre}.0000{i}.wav')

def play_random_clip_file(genre: str) -> None:
    data, fs = sf.read(get_random_clip_file(genre), dtype='float32')
    sd.play(data, fs)
