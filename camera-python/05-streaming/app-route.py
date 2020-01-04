
from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('link.html')

@app.route("/foo")
def foo():
    extns = ['Flask', 'Jinja2', 'Awesome']
    return render_template('bar.html', extns=extns)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
