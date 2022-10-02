from flask import Flask
from datetime import datetime
import re

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/api/summarize")
def summarize():
    