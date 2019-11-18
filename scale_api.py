from flask import Flask, url_for, render_template, redirect, request
from flask_cors import CORS
import serial

app = Flask(__name__)
CORS(app)

@app.route('/api', methods=('GET','POST'))
def read_serial():
    f = open('port.txt')
    port = f.readline().strip()
    ser = serial.Serial(port, 9600)
    value = int(ser.readline())
    return str(value)

