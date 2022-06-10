# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def index():
#   return render_template("index.html")

# # app.run(host="0.0.0.0", port=8000)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'