from flask import Flask, render_template
import requests, json
from api import API

app = Flask(__name__)

@app.route("/")
def home():
    # For New York:
    parameters = {
        "lat": 40.71,
        "lon": -74
    }
    response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
    times = API.datetime(response)
    return render_template("home.html", times=times)

if __name__ == "__main__":
    app.run(debug=True)
