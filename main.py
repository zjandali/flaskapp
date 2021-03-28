from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
<<<<<<< HEAD
    return render_template("templates/index.html")
=======
    return render_template("template/index.html")
>>>>>>> bb858e96014596c87c323bd790b6669c0430ea61

@app.route('/zain')
def zain():
    return render_template("templates/index.html")


if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)
