from flask import Flask, render_template, request, redirect, url_for
import os
directory = 'songs/'
link = "https://github.com/DimaG55-the-youtuber/spotifyplayer/blob/master/songs/"

app = Flask(__name__)

@app.route('/')
def index():
    songs = [{"name": filename.name.replace(".mp3", ""), "path": f"{link}{filename.name}?raw=true"} for filename in os.scandir(directory) if filename.is_file()]
    return render_template('index.html', songs=songs)