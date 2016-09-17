from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/index")
def index():
    return "this is the index"

@app.route("/contact")
def contact():
    return "Contact us!"

if __name__ == "__main__":
    app.run()
