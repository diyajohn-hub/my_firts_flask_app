from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return "Index!"

@app.route("/hello/<name>")
@app.route("/hello/<name>/")
def hello_name(name):
    try:
        response = requests.get("https://api.adviceslip.com/advice")
        data = response.json()

        live_quote = data["slip"]["advice"]
    except Exception:
        live_quote = "The code is working, but the live quote server is taking a nap"

    return render_template('test.html', name=name, quote=live_quote)    


if __name__ == "__main__":
    app.run(debug=True, port=80)