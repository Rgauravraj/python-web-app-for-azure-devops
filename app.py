from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, this is Gaurav !2.0"
    return "Hello, this is a sample Python Web App running on Flask Framework!"
    return "Welcome !"

