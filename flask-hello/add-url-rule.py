from flask import Flask, redirect, url_for

app = Flask(__name__)



def niranjan():
    return 'Hello, Niranjan!'
app.add_url_rule('/niranjan', 'niranjan', niranjan)


if __name__ == '__main__':
    app.run(debug=True)