from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, The First CICD Jenkins has begun... It was an awsom experience. </h1>"
