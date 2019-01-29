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
    machid = args.keys()[0]
    with open('license-server.log', 'w') as f:
        f.write('ip: %s, machid: %s' %(ip, machid))
    if machid == 'QyZGKUpATmNSZlRqV25acg':
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
