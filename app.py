from flask import Flask, render_template, request, redirect, url_for
import os
directory = 'songs/'

app = Flask(__name__)

@app.route('/')
def index():
    songs = [{"name": filename.name.replace(".mp3", ""), "path": filename.path} for filename in os.scandir(directory) if filename.is_file()]
    return render_template('index.html', songs=songs)