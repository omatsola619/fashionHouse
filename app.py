from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome to Fashion House"


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
    app.run(port=2500, debug=True)