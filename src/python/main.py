from flask import Flask, send_file

import src.python.basicplotutil as bpl

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<img src=/image>'

@app.route("/image")
def serve_image():
    return send_file(build_image("coastline"))

def build_image(name : str):
    return bpl.generate_map(name)