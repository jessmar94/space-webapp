from flask import Flask, render_template, request
import requests, json
from model.format import Formatter
from model.lat_long import Coordinates

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        req = request.form
        city = req.get("city")
        coords = Coordinates.lat_long(city)
        response = requests.get("http://api.open-notify.org/iss-pass.json", params=coords)
        pass_times = response.json()['response']
        times = Formatter.datetime(pass_times)
        return render_template("home.html", times=times, city=city)
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
