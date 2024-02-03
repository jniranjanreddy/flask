from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/hello/<name>')
def admin(name):
    return 'Sri '+ name


@app.route('/hello/<int:sub>')
def count(sub):
    return 'My NUmber is  =%d'%sub



if __name__ == '__main__':
    app.run(debug=True)