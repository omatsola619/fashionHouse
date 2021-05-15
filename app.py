from flask import Flask, render_template
import os


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    pass


@app.route("/admin")
def admin():
    pass


@app.route("/store/new")
def newStore():
    pass


@app.route("/stores")
def allStores():
    pass

@app.route("/store")
def store():
    pass


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)