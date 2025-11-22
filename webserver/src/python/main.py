from flask import Flask, send_file
from flask_cors import CORS

import src.python.basicplotutil as bpl

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return '<div><img src=/image1><img src=/image2></div>'

@app.route("/image1")
def serve_image_1():
    return send_file(build_image("coastline"))

@app.route("/image2")
def serve_image_2():
    return send_file(build_image("land"))

def build_image(name : str):
    return bpl.generate_map(name)