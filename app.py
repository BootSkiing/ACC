"""
Now configure with Flask! Running this will display a web API on a local port
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("mainpage.html")

if __name__ == '__main__':
    app.run(debug=False)