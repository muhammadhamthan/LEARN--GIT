from flask import Flask
app = Flask(__name__)
@app.route("/home")
def home():
    return "Welcome to home page"

app.run(port=5000,debug=True)