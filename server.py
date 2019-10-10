from flask import Flask
from flask import Response

app = Flask(__name__)

@app.route("/add/<arg1>/<arg2>")
def add(arg1, arg2):
    return str(float(arg1) + float(arg2))

@app.route("/substract/<arg1>/<arg2>")
def substract(arg1, arg2):
    return str(float(arg1) - float(arg2))

@app.route("/multiply/<arg1>/<arg2>")
def multiply(arg1, arg2):
    return str(float(arg1) * float(arg2))

@app.route("/divide/<arg1>/<arg2>")
def divide(arg1, arg2):
    if float(arg2) == 0.0:
      return Response("You cannot divide by zero!", status=403, mimetype="application/json")
    else:
      return str(float(arg1) / float(arg2))
