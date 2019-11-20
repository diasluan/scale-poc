from flask import Flask, url_for, render_template, redirect, request
from flask_cors import CORS
import serial
import re
import json

app = Flask(__name__)
CORS(app)

@app.route('/api', methods=('GET','POST'))
def read_serial():
    f = open('port.txt')
    port = f.readline().strip()
    ser = serial.Serial(port, 9600, timeout=1)
    value = ser.read(70)
    response = parse_value(value)
    return json.dumps(response)

def parse_value(str):
    match = re.findall(r'([0-9.-]+\w\w)', str)
    reponse = {
        "gross": match.group(0),
        "tare": match.group(1),
        "net": match.group(2),
        "model": "Brecknell LPS-150",
        "capacity": "150lb / 68kg",
        "d": "0.05lb / 0.02kg",
        "serial_number": "0000001"
    }
    return response 
