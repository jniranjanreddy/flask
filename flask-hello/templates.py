from flask import *

app = Flask(__name__)


# @app.route('/user/<name>')
# def message(name):
#     return render_template('base.html',name=name)

@app.route('/')
def message():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True)