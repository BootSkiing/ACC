"""
Now configured with Flask! Running this will display a web API on a local port
"""
from flask import Flask, render_template, request, flash, send_from_directory
from flask_bootstrap import Bootstrap
import src
import os

app = Flask(__name__, template_folder="./templates")
bootstrap = Bootstrap(app)


@app.route("/")
def main():
    image_names = os.listdir("./images")
    return render_template("mainpage.html", image_names=image_names)


@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("./images", filename)


@app.route("/<filename>")
def desc_page(filename):
    file = filename[:-4]
    return render_template("desc_page_template.html", file=file, filename=filename)


@app.route("/submit")
def submit():
    return render_template("submit.html")

@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/result", methods=['POST', 'GET'])
# Needs to be given data from the Neural Net
def result():
    if request.method == 'POST':
        form = request.form
        # This line will send form data to a seperate file to be processed. The returned value is the result
        # result = src.fileparse.doshit(form.essay)
        result = 0
        return render_template("result.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)
