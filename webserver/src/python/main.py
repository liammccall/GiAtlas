from flask import Flask, request, send_file
from flask_cors import CORS

import src.python.basicplotutil as bpl
import src.python.basicdb as bdb

app = Flask(__name__)
CORS(app)

@app.route("/image1")
def serve_image_1():
    return send_file(build_image("coastline"))

@app.route("/image2")
def serve_image_2():
    return send_file(build_image("land"))

@app.route("/api/save_image", methods=['PUT'])
def save_image():
    data = request.json
    file_name = data.get('file_name')
    bdb.save_file(file_name)

def build_image(name : str):
    return bpl.generate_map(name)