#!/usr/bin/env python
# Requires: python2,  flask, flask-cors
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)
CORS(app)


@app.route('/license/', methods=['GET'])
def license_():
    args = request.args.to_dict()
    ip = request.remote_addr
    query = args.keys()[0]    # Seems to correspond to Browser type. Does not identify client or video. Helps identify client compatibility.
    with open('license-server.log', 'a') as f:
        f.write('ip: %s, query: %s\n' %(ip, query))
    allowed_query = [
        'QyZGKUpATmNSZlRqV25acg',
    ]
    if query in allowed_query:
        return jsonify({
            "keys": [
                {
                    "kid": "QyZGKUpATmNSZlRqV25acg",
                    "k": "LUphTmRSZlVqWG4ycjV1OA"
                }
            ]
        })
    

@app.route('/ls')
def ls_():
    return jsonify(os.listdir('static/dash'))


app.debug=True
app.run(host='0.0.0.0', port=5000)
