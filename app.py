from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>hello world webhook configured successfully</h1>"

