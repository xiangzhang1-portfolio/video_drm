#!/usr/bin/env python
# Requires: python2,  flask, flask-cors
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)
CORS(app)


@app.route('/license/')
def license_():
    if request.args[0][0] == 'AKDf3mwC7AAGQPCwAAAP8A':  # signature of machine, i think
        return jsonify({
            "keys": [
                {
                    "kid": "JHARDFDE6CS2ECSXM64WFLBIGMHWUFFI",
                    "k": "8MQUQDSY5OUQLC0VCQ5E2B0IBPKOSCKW"
                }
            ]
        })


@app.route('/ls')
def ls_():
    return jsonify(os.listdir('static/dash'))


app.run(host='0.0.0.0', port=5000)
