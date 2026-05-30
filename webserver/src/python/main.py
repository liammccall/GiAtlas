from flask import Flask, request, send_file, json, make_response
from flask_cors import CORS

import src.python.basicplotutil as bpl
import src.python.db.basicdb as bdb
import src.python.mlinject as mlinj

# init

app = Flask(__name__)
CORS(app)

# properties



# util

def build_image_local(name : str):
    return bpl.generate_map_file(name)

def build_image(name : str):
    df = bdb.retrieve_file(name)
    return bpl.generate_map_df(df)

# api endpoints

@app.route("/geojson/<name>")
def serve_geojson(name):
    
    # df = bdb.retrieve_file(name)
    df = bdb.retrieve_file("main_map")

    # Leaflet expects EPSG:4326
    df = df.to_crs(4326)

    geojson = df.to_json()

    print(f"Returning {name}")

    response = make_response(geojson)

    response.headers["Content-Type"] = "application/json"
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"

    return response

@app.route("/image1")
def serve_image_1():
    return send_file(build_image("main_map"), mimetype="png")


bdb.save_file("land", "land")

@app.route("/image2")
def serve_image_2():
    return send_file(build_image("land"), mimetype="png")

@app.route("/api/query", methods=['POST'])
def generate_image():
    data = request.json
    file_name = data.get('file_name')
    print(request)
    print(data)
    print(f"requesting {file_name}")
    try:
        df = mlinj.llmqueryshapedb(file_name)
        print("success")
    except Exception as e:
        print(e)
        df = bdb.retrieve_file("land")

    # Leaflet expects EPSG:4326
    df = df.to_crs(4326)

    geojson = df.to_json()

    response = make_response(geojson)

    response.headers["Content-Type"] = "application/json"
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"

    return response

@app.route("/api/save_image", methods=['POST'])
def save_image():
    data = request.json
    file_name = data.get('file_name')
    print(request)
    print(data)
    print(f"saving {file_name}")
    bdb.save_natural_earth(file_name, file_name)
    return json.jsonify({"status":"success","message":f"Saved {file_name}"})