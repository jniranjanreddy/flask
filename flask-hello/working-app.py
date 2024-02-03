from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/admin')
def admin():
    return 'Hello, Admin!'

@app.route('/student')
def student():
    return 'Hello, student!'

@app.route('/staff')
def staff():
    return 'Hello, staff!'


@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    if name == 'student':
        return redirect(url_for('student'))
    if name == 'staff':
        return redirect(url_for('staff'))
    






def hello_world():
    return 'Hello, Flask!'
# app.add_url_rule('/hello', 'hello', hello_world)










if __name__ == '__main__':
    app.run(debug=True)