from flask import Flask
from datetime import datetime
import re
from summarization import Summarize

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/api/summarize/<text>")
def summarize(text):
    return Summarize(text)