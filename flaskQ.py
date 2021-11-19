from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    dictionary = {"name": "むっちゃん", "age": 21, "address": "東京都"}
    flag = False

    return render_template('flaskQ.html', dictionary = dictionary, flag = flag)


if __name__ == "__main__":
    app.debug = True
    app.run(port = 8000)