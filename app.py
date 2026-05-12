from flask import flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World! This is my first Flask website."

if __name__ ++ "__main__":
    app.run(debug=True)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Home Page"

@app.route("/about")
def about():
    return "This is the About Page"

@app.route("/contact")
def contact():
    return "Contact us at [email protected]"

if __name__ == "__main__":
    app.run(debug=True)