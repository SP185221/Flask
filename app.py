from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/home")
def home():
    return "<h1>This is Home page!</h1>"

@app.route("/about")
def about():
    return "<h1>This is about Page!</h1>"

if __name__ == "__main__":
    app.run(debug = True , port = 8000)