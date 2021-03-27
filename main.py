from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("template/index.html")

@app.route('/zain')
def zain():
    return render_template("minimal-mistakes/index.html")


if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)
