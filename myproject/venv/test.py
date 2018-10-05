from flask import Flask
app = Flask(__name__)

@app.route("/<string:name>")
def hello_world(name):
    name = name.capitalize()
    return f"<h1>Hello, {name}</h1>"
