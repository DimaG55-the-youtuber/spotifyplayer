from flask import Flask, render_template, request, redirect, url_for
import os

directory = 'songs/'

app = Flask(__name__)

@app.route('/')
def index():
    songs = [{"name": filename.name, "path": filename.path} for filename in os.scandir(directory) if filename.is_file()]
    for i in songs:
        uh = i["name"].replace('[SPOTIFY-DOWNLOADER.COM]', '_')
        uh = uh.replace('.mp3', '')
        uh = uh.replace('_', ' ')
        songs.remove(i)
        songs.append({"name": uh, "path": i["path"]})
    return render_template('index.html', songs=songs)