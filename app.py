from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Server restarted</h1>"

@app.route("/home")
def home():
    return "<h1>This is the home page</h1>"

