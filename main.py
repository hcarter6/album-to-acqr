# to run locally:
# export FLASK_APP=main.py
# flask run

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from flask import Flask, redirect, url_for, render_template, request

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def home():
	if request.method == "POST":
		ttl = request.form["title"]
		results = spotify.search(q='album:' + ttl, type='album')
		name = results['albums']['items'][0]['name']
		url = results['albums']['items'][0]['images'][0]['url']
		return render_template("index.html", ttl=name, url=url)
	return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)