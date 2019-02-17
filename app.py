"""
Now configure with Flask! Running this will display a web API on a local port
"""
from flask import Flask, render_template, request, flash, send_from_directory
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route("/")
def main():
    image_names = os.listdir("./images")
    return render_template("mainpage.html", image_names = image_names)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("./images", filename)


if __name__ == '__main__':
    app.run(debug=True)
