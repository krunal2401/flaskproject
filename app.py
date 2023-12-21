from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, The First CICD Jenkins has begun.</h1>"

@app.route("/home")
def home():
    return "<h1>this is Home Page/</h1>"
