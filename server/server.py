from flask import Flask, jsonify, make_response
import json

app = Flask(__name__)

@app.route('/<string:package>/<string:version>', methods = ['GET'])
def get(package, version):
    package = package.lower()
    try:
        if "apache" in package:
            package = "httpd"
        elif "" in package:
            package = ""
        with open('target_' + package + '_cve.json') as file:
            data = json.load(file)
            return make_response(jsonify(data[version]), 200)
    except:
        return make_response(jsonify({"failure": "failure"}), 500)

app.run()