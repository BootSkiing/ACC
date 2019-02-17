"""
Now configure with Flask! Running this will display a web API on a local port
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    print('Welcome to Awesome project')
    return "Welcome to Awesome project"