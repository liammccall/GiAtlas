from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<img src=/image>'

@app.route("/image")
def serve_image():
    return send_file("/app/out/combined.png")