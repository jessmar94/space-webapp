from flask import Flask, render_template, request
import requests, json
from model.api import API

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        req = request.form
        city = req.get("city")
        parameters = {
            "lat": 40.71,
            "lon": -74
        }
        response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
        times = API.datetime(response)
        return render_template("home.html", times=times, city=city)
    return render_template("home.html")
        # return redirect(request.url)
    # For New York:
    # parameters = {
    #     "lat": 40.71,
    #     "lon": -74
    # }
    # response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
    # times = API.datetime(response)
    # return render_template("home.html", times=times)

if __name__ == "__main__":
    app.run(debug=True)
