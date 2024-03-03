from flask import Flask, render_template, request, send_file, send_from_directory
import random
from util.concentration import get_prob

app = Flask(__name__)

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
genres = [
    "blues", "classical", "country", "disco", "hiphop",
    "jazz", "metal", "pop", "reggae", "rock"
]


@app.route("/")
def questions():
    return render_template("survey.html")

@app.route("/results", methods=["POST"])
def results():
    pace_preference = request.form.get("pace")
    beat_preference = request.form.get("beat")
    instrumental_preference = request.form.get("instrumental")
    energy_preference = request.form.get("energy")
    genre_count = {genre: 0 for genre in genres}
    for preference_set, genre_set in genre_mappings.items():
        if (pace_preference, beat_preference, instrumental_preference, energy_preference) == preference_set:
            for genre in genre_set:
                genre_count[genre] += 1
    sorted_genres = sorted(genre_count.keys(), key=lambda x: genre_count[x], reverse=True)
    top_three_genres = set(sorted_genres[:3])
    print(top_three_genres)
    return render_template("results.html", genres=list(top_three_genres))

@app.route("/test")
def measure_music_concentration():
    scores = request.args.get("scores", "").split(",")
    if len(scores) == 10:
        return str(max(map(float, scores)))
    genre = genres[len(scores)]
    music_file = f"{genre}.0000{random.randint(0, 9)}.wav"
    return render_template("music_test.html", music_file="/music/" + genre + "/" + music_file)

@app.route("/music/<path:filename>")
def music(filename):
    return send_from_directory("genre_clip_data", filename)

@app.route("/get_concentration_score", methods=["POST"])
def get_concentration_score():
    return str(get_prob())

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)