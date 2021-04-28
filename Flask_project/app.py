from flask import Flask

app = Flask(__name__)

@app.route("/hi")
def home_page():
    return "hi how are you"

if __name__ == '__main__':
    app.run()
    