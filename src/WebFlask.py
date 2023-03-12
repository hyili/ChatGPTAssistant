#!python3

from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
import os
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'S3CR3T11'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('echo request')
def echo(json):
    emit('echo response', json)

@socketio.on('markdown request')
def markdown():
    with open("markdown/markdown.html") as md:
        md_resp = md.read();
        emit('markdown response', md_resp)

def run_flask():
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    with open("markdown/markdown.html", "w") as md:
        md.write("Initialized!")
    print("Connect to http://127.0.0.1:5000/ for chat history.")
    socketio.run(app)
