import flask
from flask import Flask, request, send_file
import subprocess
import sys
from pathlib import Path

app = Flask(__name__)

@app.route("/simulate", methods=["POST"])
def simulate():

    data = request.json

    theta1 = str(data["theta1"])
    theta2 = str(data["theta2"])
    theta3 = str(data["theta3"])

    subprocess.run([
        sys.executable,
        "pendy.py",
        theta1,
        theta2,
        theta3
    ])

    gif = Path("pendulum.gif")

    return send_file(gif, mimetype="image/gif")


if __name__ == "__main__":
    app.run()
